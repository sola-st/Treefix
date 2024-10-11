# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
sparsify = lambda m: m * (m > 0)
a_dense_shape = [53, 65, 127]
b_dense_shape = [53, 127, 67]
a_mats = sparsify(
    (np.random.randn(*a_dense_shape) +
     1.j * np.random.randn(*a_dense_shape))).astype(np.complex64)
b_mats = (np.random.randn(*b_dense_shape) +
          1.j * np.random.randn(*b_dense_shape)).astype(np.complex64)
a_sm = dense_to_csr_sparse_matrix(a_mats)
c_t = sparse_csr_matrix_ops.sparse_matrix_mat_mul(
    a_sm, b_mats, conjugate_output=True)

c_dense_t = math_ops.conj(test_util.matmul_without_tf32(a_mats, b_mats))
self.assertAllEqual(c_t.shape, c_dense_t.shape)
c_t_value, c_dense_t_value = self.evaluate((c_t, c_dense_t))

self.assertAllClose(c_t_value, c_dense_t_value, atol=1e-5, rtol=1e-5)
