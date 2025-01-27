# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.float32, np.double]:
    x = np.array([1, 2], dtype=dtype)
    y = np.array([[1, 2]], dtype=dtype)
    # The inputs 'x' and 'y' must have the same shape.
    with self.assertRaisesRegex(
        (ValueError, errors.InvalidArgumentError),
        "Shapes must be equal rank|must be of the same shape"):
        math_ops.approximate_equal(x, y)
