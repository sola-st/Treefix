# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Reduce an empty tensor to a nonempty tensor
x = np.zeros((5, 0))
self._compareAll(x, [1])
