# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = sparse_ops.from_dense(
    np.array([[3, 0, 1, 0], [0, 0, 0, 0], [5, 0, 4, 4]], dtype=np.int32))
weights = ragged_factory_ops.constant([[6, 0.5, 2], [14], [10, 0.25, 5, 3]])
with self.assertRaisesRegex(ValueError, "must be a SparseTensor"):
    self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
