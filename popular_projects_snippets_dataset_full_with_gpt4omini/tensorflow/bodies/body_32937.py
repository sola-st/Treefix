# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
density = 0.05
# pylint: disable=g-long-lambda
sparsify = lambda m: array_ops.where(m > 1. - density, m,
                                     array_ops.zeros_like(m))
# pylint: enable=g-long-lambda

for batch_size in [1, 16]:
    for num_threads in [1, 4, 12]:
        dense_shape = [batch_size, 250, 250]

        for device in [CPU, GPU]:
            if device == GPU and not test_util.is_gpu_available():
                continue

            with ops.Graph().as_default(), ops.device(device):
                x_mats = sparsify(
                    random_ops.random_uniform(dense_shape, dtype=dtypes.float32))
                y_mats = sparsify(
                    random_ops.random_uniform(dense_shape, dtype=dtypes.float32))

                nnz = array_ops.shape(array_ops.where(x_mats))[0] + array_ops.shape(
                    array_ops.where(y_mats))[0]
                ratio = math_ops.cast(nnz,
                                      dtypes.float32) / (2 * np.prod(dense_shape))

                x_sm = dense_to_csr_sparse_matrix(x_mats)
                y_sm = dense_to_csr_sparse_matrix(y_mats)

                xy_sparse = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul(
                    x_sm, y_sm, type=dtypes.float32)

                with session.Session(
                    config=config_pb2.ConfigProto(
                        intra_op_parallelism_threads=num_threads)) as sess:
                    nnz_value, ratio_value = self.evaluate((nnz, ratio))
                    name_template = (
                        "sparse_matrix_sparse_matmul_%s_N_%d_batch_size_%d_threads_%d"
                    )
                    device_str = "cpu" if device == CPU else "gpu"
                    self.run_op_benchmark(
                        sess,
                        xy_sparse.op,
                        name=name_template %
                        (device_str, dense_shape[-1], batch_size, num_threads),
                        extras={
                            "percentage_nonzero": ratio_value,
                            "num_nonzero": nnz_value
                        },
                        min_iters=50)
