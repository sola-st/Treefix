# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
x = np.zeros(200, dtype=dtype)

# Check that argmin and argmax match numpy along the primary axis for
# breaking ties.
self._testBothArg(math_ops.argmax, x, 0, x.argmax())
self._testBothArg(math_ops.argmin, x, 0, x.argmin())

# Check that argmin and argmax match numpy along axis=1 for
# breaking ties.
x = np.array([[0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1]], dtype=dtype)
self._testBothArg(math_ops.argmax, x, 1, x.argmax(axis=1))
self._testBothArg(math_ops.argmin, x, 1, x.argmin(axis=1))
