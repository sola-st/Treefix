# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.arange(-6, 6, 2).reshape(1, 3, 2).astype(np.int32)
self._compareCpu(x, np.abs, math_ops.abs)
self._compareCpu(x, np.abs, _ABS)
self._compareBoth(x, np.negative, math_ops.negative)
self._compareBoth(x, np.negative, _NEG)
self._compareBoth(x, np.square, math_ops.square)
self._compareCpu(x, np.sign, math_ops.sign)

self._compareBothSparse(x, np.abs, math_ops.abs)
self._compareBothSparse(x, np.negative, math_ops.negative)
self._compareBothSparse(x, np.square, math_ops.square)
self._compareBothSparse(x, np.sign, math_ops.sign)
