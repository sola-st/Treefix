# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with self.cached_session():
    np_val = np.random.rand(4, 4, 4, 4).astype(np.float32)
    c = constant_op.constant(np_val)
    c_sparse = math_ops._as_indexed_slices(c)
    c_sparse = indexed_slices.IndexedSlices(
        c_sparse.values,
        math_ops.cast(c_sparse.indices, dtypes.int64), c_sparse.dense_shape)
    self.assertAllEqual(np_val.shape, c_sparse.dense_shape)
    c_dense = math_ops.multiply(c_sparse, 1.0)
    self.assertAllClose(np_val, self.evaluate(c_dense))
