# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
x = np.arange(200, dtype=np.float32).astype(dtype)
np.random.shuffle(x)

# Check that argmin and argmax match numpy along the primary axis
self._testBothArg(math_ops.argmax, x, 0, x.argmax())
self._testBothArg(math_ops.argmin, x, 0, x.argmin())
