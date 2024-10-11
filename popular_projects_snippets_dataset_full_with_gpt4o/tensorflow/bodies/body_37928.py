# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.arange(1, 13, 2).reshape(1, 3, 2).astype(np.uint32)
y = np.arange(1, 7, 1).reshape(1, 3, 2).astype(np.uint32)
self._compareBoth(x, y, np.true_divide, math_ops.truediv)
self._compareBoth(x, y, np.floor_divide, math_ops.floordiv)
self._compareBoth(x, y, np.true_divide, _TRUEDIV)
self._compareBoth(x, y, np.floor_divide, _FLOORDIV)
