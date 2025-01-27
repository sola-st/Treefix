# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
a_dense_shape = [53, 65, 127]
a_mats = sparsify(np.random.randn(*a_dense_shape)).astype(np.float32)
b = np.float32(3.5)
expected = a_mats * b
a_sm = dense_to_csr_sparse_matrix(a_mats)
c_t = sparse_csr_matrix_ops.sparse_matrix_mul(a_sm, b)
c_dense_t = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    c_t, dtypes.float32)
c_dense_t_value = self.evaluate(c_dense_t)

self.assertAllClose(expected, c_dense_t_value)
