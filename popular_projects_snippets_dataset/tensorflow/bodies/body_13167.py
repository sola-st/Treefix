# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = constant_op.constant([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],
                         dtype=dtypes.float64)
y, segments = nn_ops.isotonic_regression(x, decreasing=False)
self.assertAllClose(y, x)
self.assertAllClose(segments, [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])

y, segments = nn_ops.isotonic_regression(x, decreasing=True)
self.assertAllClose(
    y,
    [
        [2, 2, 2, 2, 2],  # Average of the inputs.
        [7, 7, 7, 7, 7]
    ])
self.assertAllClose(segments, array_ops.zeros((2, 5)))

# pylint: disable=invalid-unary-operand-type
y, segments = nn_ops.isotonic_regression(-x, decreasing=True)
self.assertAllClose(segments, [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])

self.assertAllClose(y, -x)
y, segments = nn_ops.isotonic_regression(-x, decreasing=False)
self.assertAllClose(
    -y,
    [
        [2, 2, 2, 2, 2],  # Average of the inputs.
        [7, 7, 7, 7, 7]
    ])
self.assertAllClose(segments, array_ops.zeros((2, 5)))
