# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.rand(1, 3, 2) * 100.
# ensure x != y
y = x + (np.random.randint(2, size=x.shape) - .5) * 2  # -1 or +1
self._compareGradientX(math_ops.maximum, x, y)
self._compareGradientY(math_ops.maximum, x, y)
self._compareGradientX(math_ops.minimum, x, y)
self._compareGradientY(math_ops.minimum, x, y)
