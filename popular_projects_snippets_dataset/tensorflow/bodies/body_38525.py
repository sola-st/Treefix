# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.arange(-6, 6, 2).reshape(1, 3, 2).astype(np.int8)
self._compareCpu(x, np.abs, math_ops.abs)
self._compareCpu(x, np.abs, _ABS)
self._compareBoth(x, np.negative, math_ops.negative)
self._compareBoth(x, np.negative, _NEG)
self._compareBoth(x, np.sign, math_ops.sign)
