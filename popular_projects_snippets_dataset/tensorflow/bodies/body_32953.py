# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
if not self._gpu_available:
    exit()

a_indices = np.array([[0, 0], [2, 3], [2, 4], [3, 0]])
a_values = [1.0, 5.0, -1.0, -2.0]
a_dense_shape = [5, 6]

a_st = sparse_tensor.SparseTensor(a_indices, a_values, a_dense_shape)
a_st = math_ops.cast(a_st, dtypes.float32)
a_sm = sparse_csr_matrix_ops.CSRSparseMatrix(a_st)
self.assertEqual(a_sm.shape, a_dense_shape)

a_st_rt = a_sm.to_sparse_tensor()
a_st_rt = self.evaluate(a_st_rt)

self.assertAllEqual(a_indices, a_st_rt.indices)
self.assertAllClose(a_values, a_st_rt.values)
self.assertAllEqual(a_dense_shape, a_st_rt.dense_shape)
