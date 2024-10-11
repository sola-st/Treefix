# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.uint8)
y = np.arange(1, 7, 1).reshape(1, 3, 2).astype(np.uint8)
self._compareBoth(x, y, np.add, math_ops.add)
self._compareBoth(x, y, np.subtract, math_ops.subtract)
self._compareBoth(x, y, np.subtract, _SUB)
