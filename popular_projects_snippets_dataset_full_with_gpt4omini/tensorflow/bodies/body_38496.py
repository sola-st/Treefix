# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
shape = (3, 2, 4, 5, 6, 3, 7)
x = np.arange(
    functools.reduce(lambda x, y: x * y, shape),
    dtype=np.float32).astype(dtype)
np.random.shuffle(x)
x = x.reshape(shape)

# Check that argmin and argmax match numpy along all axes
for axis in range(-7, 7):
    self._testBothArg(math_ops.argmax, x, axis, x.argmax(axis))
    self._testBothArg(math_ops.argmin, x, axis, x.argmin(axis))
