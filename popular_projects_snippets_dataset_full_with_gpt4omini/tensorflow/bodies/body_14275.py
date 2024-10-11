# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = sparse_ops.from_dense(
    np.array([[3, 0, 1, 0], [0, 0, 0, 0], [5, 0, 4, 4]], dtype=np.int32))
weights = sparse_ops.from_dense(
    np.array([[3, 0, 1, 0], [0, 0, 0, 0], [5, 0, 4, 4], [0, 0, 0, 0]],
             dtype=np.int32))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "must have the same dense shape"):
    self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
