# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m.real > 0)
dense_shape = [5, 7, 13]
a_mats = sparsify(
    (np.random.randn(*dense_shape) + 1.j * np.random.randn(*dense_shape))
    .astype(np.complex64))
a_sm = sparse_csr_matrix_ops.CSRSparseMatrix(a_mats)
a_sm_conj = a_sm.conj()
self.assertIsInstance(a_sm_conj, sparse_csr_matrix_ops.CSRSparseMatrix)
a_sm_conj_dense = a_sm_conj.to_dense()
a_sm_conj_dense = self.evaluate(a_sm_conj_dense)
self.assertAllClose(a_mats.conj(), a_sm_conj_dense)
