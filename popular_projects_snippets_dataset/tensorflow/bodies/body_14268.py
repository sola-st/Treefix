# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = np.array([[3, 2, 1], [5, 4, 4]], dtype=np.int32)
weights = sparse_ops.from_dense(
    np.array([[3, 0, 1, 0], [0, 0, 0, 0], [5, 0, 4, 4]], dtype=np.int32))
with self.assertRaisesRegex(ValueError, "must be a tf.Tensor"):
    self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
