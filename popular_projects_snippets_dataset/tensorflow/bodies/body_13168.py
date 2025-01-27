# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = constant_op.constant([[0, 6, 2, 8, 4], [5, 1, 7, 3, 9]],
                         dtype=dtypes.float64)
y, segments = nn_ops.isotonic_regression(x, decreasing=True, axis=0)
self.assertAllClose(
    y,
    [
        [2.5, 6, 4.5, 8, 6.5],  # Either identity or average.
        [2.5, 1, 4.5, 3, 6.5]
    ])
self.assertAllClose(segments, [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0]])
