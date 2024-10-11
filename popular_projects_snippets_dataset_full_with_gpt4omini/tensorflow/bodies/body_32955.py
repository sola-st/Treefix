# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
if not self._gpu_available:
    exit()

dense_shape = [5, 7, 13]
a_mats = np.random.randn(*dense_shape).astype(np.float32)
indices = np.array([[0, 0, 0],
                    [1, 0, 0]], dtype=np.int64)

a_sm = sparse_csr_matrix_ops.CSRSparseMatrix(a_mats, indices=indices)
self.assertEqual(a_sm.shape, a_mats.shape)

a_sm_st = a_sm.to_sparse_tensor()
a_sm_st = self.evaluate(a_sm_st)

# Count number of nonzero entries for each batch using bincount.
self.assertAllEqual(indices, a_sm_st.indices)
self.assertAllEqual(dense_shape, a_sm.shape)
self.assertAllEqual(dense_shape, a_sm_st.dense_shape)
self.assertAllClose([a_mats[tuple(x)] for x in indices], a_sm_st.values)
