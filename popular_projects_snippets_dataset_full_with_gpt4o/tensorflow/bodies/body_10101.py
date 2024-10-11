# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py

@def_function.function(jit_compile=True)
def approximate_equal(x, y):
    exit(math_ops.approximate_equal(x, y))

for dtype in [np.float32, np.double]:
    x = np.array([1, 2], dtype=dtype)
    y = np.array([[1, 2]], dtype=dtype)
    with self.assertRaisesRegex(
        (ValueError, errors.InvalidArgumentError),
        "Shapes must be equal rank|must be of the same shape"):
        approximate_equal(x, y)
