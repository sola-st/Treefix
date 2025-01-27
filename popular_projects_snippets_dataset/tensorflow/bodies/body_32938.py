# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
sparsity = 0.05

for batch_size in [1, 16]:
    for num_threads in [1, 4, 12]:
        dense_shape = [batch_size, 750, 750]

        for device in [CPU, GPU]:
            if device == GPU and not test_util.is_gpu_available():
                continue

            with ops.Graph().as_default(), ops.device(device):
                mats = random_ops.random_uniform(dense_shape, dtype=dtypes.float32)
                mats_locs = array_ops.where(mats > 1.0 - sparsity)

                sparse_matrices = sparse_csr_matrix_ops.dense_to_csr_sparse_matrix(
                    mats, mats_locs)
                dense_matrices = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
                    sparse_matrices, type=dtypes.float32)
                nnz = math_ops.reduce_sum(
                    sparse_csr_matrix_ops.sparse_matrix_nnz(sparse_matrices))
                ratio = math_ops.cast(nnz, dtypes.float32) / np.prod(dense_shape)

                with session.Session(
                    config=config_pb2.ConfigProto(
                        intra_op_parallelism_threads=num_threads)) as sess:
                    nnz_value, ratio_value = self.evaluate((nnz, ratio))
                    device_str = "cpu" if device == CPU else "gpu"
                    name_template = (
                        "dense_to_sparse_matrix_%s_N_%d_batch_size_%d_num_threads_%d")
                    self.run_op_benchmark(
                        sess,
                        sparse_matrices.op,
                        name=name_template %
                        (device_str, dense_shape[-1], batch_size, num_threads),
                        extras={
                            "percentage_nonzero": ratio_value,
                            "num_nonzero": nnz_value,
                        },
                        min_iters=50)
                    name_template = (
                        "sparse_matrix_to_dense_%s_N_%d_batch_size_%d_num_threads_%d")
                    self.run_op_benchmark(
                        sess,
                        dense_matrices.op,
                        name=name_template %
                        (device_str, dense_shape[-1], batch_size, num_threads),
                        extras={
                            "percentage_nonzero": ratio_value,
                            "num_nonzero": nnz_value,
                        },
                        min_iters=50)
