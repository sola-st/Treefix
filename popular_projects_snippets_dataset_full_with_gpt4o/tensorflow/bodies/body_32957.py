# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
if not self._gpu_available:
    exit()

for conjugate in False, True:
    sparsify = lambda m: m * (m > 0)
    dense_shape = [5, 7, 13]
    a_mats = sparsify((np.random.randn(*dense_shape) +
                       1.j * np.random.randn(*dense_shape))).astype(
                           np.complex64)
    expected = np.transpose(a_mats, (0, 2, 1))
    if conjugate:
        expected = np.conj(expected)
    a_sm = sparse_csr_matrix_ops.CSRSparseMatrix(a_mats)
    if conjugate:
        a_sm_t = a_sm.hermitian_transpose()
    else:
        a_sm_t = a_sm.transpose()
    self.assertIsInstance(a_sm_t, sparse_csr_matrix_ops.CSRSparseMatrix)
    a_sm_t_dense = a_sm_t.to_dense()
    a_sm_t_dense = self.evaluate(a_sm_t_dense)
    self.assertAllClose(expected, a_sm_t_dense)
