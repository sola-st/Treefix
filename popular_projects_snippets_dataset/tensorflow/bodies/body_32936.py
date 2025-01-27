# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# num_rows, device, transpose.
cases = [
    [2000, CPU, False],
    [8000, CPU, False],
    [12000, CPU, False],
    [2000, CPU, True],
    [8000, CPU, True],
    [12000, CPU, True],
]
seed = 42

for num_rows, device, transpose in cases:
    if device == GPU and not test_util.is_gpu_available():
        continue
    for num_threads in [1, 2, 4, 6, 8, 10]:
        device_str = "cpu" if device == CPU else "gpu"
        w_dense_shape = [num_rows, num_rows]
        x_dense_shape = [num_rows, 1]

        with ops.Graph().as_default(), ops.device(device):
            random_seed.set_random_seed(seed)
            x = random_ops.random_normal(x_dense_shape, dtype=dtypes.float32)
            w_np = sparse.rand(
                w_dense_shape[0],
                w_dense_shape[1],
                density=0.01,
                dtype=np.float32,
                random_state=np.random.RandomState(seed))
            w_st = sparse_tensor.SparseTensor(
                zip(w_np.row, w_np.col), w_np.data, w_np.shape)
            w_st = sparse_ops.sparse_reorder(w_st)

            nnz = array_ops.shape(w_st.values)[0]
            ratio = math_ops.cast(nnz, dtypes.float32) / np.prod(w_np.shape)

            w_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
                w_st.indices, w_st.values, w_st.dense_shape)
            xw_sparse_matrix = sparse_csr_matrix_ops.sparse_matrix_mat_mul(
                w_sm,
                x,
                transpose_a=transpose,
                transpose_b=False,
                transpose_output=False)
            xw_sparse_tensor = sparse_ops.sparse_tensor_dense_matmul(
                w_st, x, adjoint_a=transpose, adjoint_b=False)

            with session.Session(
                config=config_pb2.ConfigProto(
                    intra_op_parallelism_threads=num_threads)) as sess:
                nnz_value, ratio_value = sess.run((nnz, ratio))
                name_template = ("mat_vec_mul_%s_%s_W_%d_transpose_%s_threads_%d")
                self.run_op_benchmark(
                    sess,
                    xw_sparse_matrix.op,
                    name=name_template %
                    (device_str, "sparse_matrix", num_rows, transpose, num_threads),
                    extras={
                        "percentage_nonzero": ratio_value,
                        "num_nonzero": nnz_value,
                    },
                    min_iters=10)
                self.run_op_benchmark(
                    sess,
                    xw_sparse_tensor.op,
                    name=name_template %
                    (device_str, "sparse_tensor", num_rows, transpose, num_threads),
                    extras={
                        "percentage_nonzero": ratio_value,
                        "num_nonzero": nnz_value,
                    },
                    min_iters=10)
