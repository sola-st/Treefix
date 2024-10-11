# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
sp_empty = self._SparseTensor_4x6_empty()
sparse_splits0 = sparse_ops.sparse_split(
    sp_input=sp_empty, num_split=2, axis=0)
sparse_splits1 = sparse_ops.sparse_split(
    sp_input=sp_empty, num_split=2, axis=1)
empty_inds = np.empty(shape=(0, 2), dtype=np.int64)
self.assertAllEqual(sparse_splits0[0].indices, empty_inds)
self.assertAllEqual(sparse_splits0[0].values, [])
self.assertAllEqual(sparse_splits0[0].dense_shape, [2, 6])
self.assertAllEqual(sparse_splits0[1].indices, empty_inds)
self.assertAllEqual(sparse_splits0[1].values, [])
self.assertAllEqual(sparse_splits0[1].dense_shape, [2, 6])
self.assertAllEqual(sparse_splits1[0].indices, empty_inds)
self.assertAllEqual(sparse_splits1[0].values, [])
self.assertAllEqual(sparse_splits1[0].dense_shape, [4, 3])
self.assertAllEqual(sparse_splits1[1].indices, empty_inds)
self.assertAllEqual(sparse_splits1[1].values, [])
self.assertAllEqual(sparse_splits1[1].dense_shape, [4, 3])
