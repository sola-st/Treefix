# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = np.array([[3, 2, 1], [5, 4, 4]], dtype=np.int32)
weights = ragged_factory_ops.constant([[6, 0.5, 2], [14], [10, 0.25, 5, 3]])
with self.assertRaisesRegex(ValueError, "must be a tf.Tensor"):
    self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
