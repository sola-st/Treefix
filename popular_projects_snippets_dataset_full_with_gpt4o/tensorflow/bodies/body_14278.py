# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = ragged_factory_ops.constant([[6, 1, 2], [14], [10, 1, 5, 3]])
weights = ragged_factory_ops.constant([[6, 0.5, 2], [], [10, 0.25, 5, 3]])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "must have the same row splits"):
    self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
