# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not test_util.is_gpu_available():
    exit()

sparsify = lambda m: array_ops.where(m > 2, m, array_ops.zeros_like(m))

# XW, X dense and W sparse
# X is shaped [{1, 8, 16}, 2000]
# W is shaped [2000, 4000]

for batch_size in [1, 8, 16]:
    x_dense_shape = [batch_size, 2000]
    w_dense_shape = [2000, 4000]

    with ops.Graph().as_default(), ops.device("/gpu:0"):
        x_mats = random_ops.random_normal(x_dense_shape, dtype=dtypes.float32)
        w_mats = sparsify(
            random_ops.random_normal(w_dense_shape, dtype=dtypes.float32))
        nnz = array_ops.shape(array_ops.where(w_mats))[0]
        ratio = math_ops.cast(nnz, dtypes.float32) / np.prod(w_dense_shape)
        w_sm = dense_to_csr_sparse_matrix(w_mats)
        with ops.name_scope("w_sm_var"):
            w_sm_var = variable_scope.get_variable(
                "sm", initializer=w_sm, use_resource=True)
            w_sm_var_v = w_sm_var.read_value()
        with ops.name_scope("w_var"):
            w_var = variable_scope.get_variable(
                "sm_dense", initializer=w_mats, use_resource=True)
            w_var_v = w_var.read_value()
        with ops.name_scope("b"):
            x = variable_scope.get_variable(
                "b", initializer=x_mats, use_resource=True)
            x_v = x.read_value()
        # X*W = (W'*X')'
        xw_sparse = sparse_csr_matrix_ops.sparse_matrix_mat_mul(
            w_sm_var_v,
            x_v,
            transpose_a=True,
            transpose_b=True,
            transpose_output=True)
        xw_dense = math_ops.matmul(x_v, w_var_v)

        with session.Session() as sess:
            self.evaluate(
                [w_var.initializer, w_sm_var.initializer, x.initializer])
            nnz_value, ratio_value = self.evaluate((nnz, ratio))
            name_template = (
                "sparse_matrix_mat_mul_gpu_%s_W_2000x4000_batch_size_%d")
            self.run_op_benchmark(
                sess,
                xw_sparse.op,
                name=name_template % ("sparse", batch_size),
                extras={
                    "percentage_nonzero": ratio_value,
                    "num_nonzero": nnz_value
                },
                min_iters=50)
            self.run_op_benchmark(
                sess,
                xw_dense.op,
                name=name_template % ("dense", batch_size),
                extras={
                    "percentage_nonzero": ratio_value,
                    "num_nonzero": nnz_value
                },
                min_iters=50)
