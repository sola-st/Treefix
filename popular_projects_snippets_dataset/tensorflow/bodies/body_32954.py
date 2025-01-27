# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [5, 7, 13]
a_mats = sparsify(np.random.randn(*dense_shape)).astype(np.float32)

a_sm = sparse_csr_matrix_ops.CSRSparseMatrix(a_mats)
self.assertEqual(a_sm.shape, a_mats.shape)

a_sm_rt = a_sm.to_dense()
a_sm_nnz = a_sm.nnz()
a_sm_nnz, a_sm_rt = self.evaluate([a_sm_nnz, a_sm_rt])

# Count number of nonzero entries for each batch using bincount.
nz = np.bincount(a_mats.nonzero()[0], minlength=a_mats.shape[0])
self.assertAllEqual(nz, a_sm_nnz)
self.assertAllClose(a_mats, a_sm_rt)
