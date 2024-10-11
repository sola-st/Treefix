# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
sparsify = lambda m: m * (m > 0)

for (transpose_a, transpose_b) in ((False, False), (False, True),
                                   (True, False), (True, True)):
    for (adjoint_a, adjoint_b) in ((False, False), (False, True),
                                   (True, False), (True, True)):
        if (transpose_a and adjoint_a) or (transpose_b and adjoint_b):
            continue

        a_dense_shape = ([53, 127, 65]
                         if transpose_a or adjoint_a else [53, 65, 127])
        b_dense_shape = ([53, 67, 127]
                         if transpose_b or adjoint_b else [53, 127, 67])

        a_mats = sparsify(np.random.randn(*a_dense_shape)).astype(np.float32)
        b_mats = sparsify(np.random.randn(*b_dense_shape).astype(np.float32))

        a_sm = dense_to_csr_sparse_matrix(a_mats)
        b_sm = dense_to_csr_sparse_matrix(b_mats)
        c_sm = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul(
            a_sm,
            b_sm,
            type=dtypes.float32,
            transpose_a=transpose_a,
            adjoint_a=adjoint_a,
            transpose_b=transpose_b,
            adjoint_b=adjoint_b)
        c_sm_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
            c_sm, dtypes.float32)
        c_dense_t = test_util.matmul_without_tf32(
            a_mats,
            b_mats,
            transpose_a=transpose_a,
            adjoint_a=adjoint_a,
            transpose_b=transpose_b,
            adjoint_b=adjoint_b)
        c_dense_t_value, c_sm_dense_value = self.evaluate(
            (c_dense_t, c_sm_dense))

        self.assertAllClose(c_sm_dense_value, c_dense_t_value)
