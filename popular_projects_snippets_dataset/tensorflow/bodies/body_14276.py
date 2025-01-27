# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = ragged_factory_ops.constant([[6, 1, 2], [14], [10, 1, 5, 3]])
weights = np.array([[3, 2, 1], [5, 4, 4]], dtype=np.int32)
with self.assertRaisesRegex(ValueError, "must be a RaggedTensor"):
    self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
