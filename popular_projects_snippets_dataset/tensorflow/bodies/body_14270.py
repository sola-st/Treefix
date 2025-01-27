# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
x = np.array([[3, 2, 1], [5, 4, 4]], dtype=np.int32)
weights = np.array([[3, 2], [5, 4], [4, 3]])
# Note: Eager mode and graph mode throw different errors here. Graph mode
# will fail with a ValueError from the shape checking logic, while Eager
# will fail with an InvalidArgumentError from the kernel itself.
if context.executing_eagerly():
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "must have the same shape"):
        self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
else:
    with self.assertRaisesRegex(ValueError, "both shapes must be equal"):
        self.evaluate(bincount_ops.sparse_bincount(x, weights=weights, axis=-1))
