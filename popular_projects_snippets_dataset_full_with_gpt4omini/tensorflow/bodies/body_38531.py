# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.arange(-6 << 40, 6 << 40, 2 << 40).reshape(1, 3, 2).astype(np.int64)
self._compareCpu(x, np.abs, math_ops.abs)
self._compareCpu(x, np.abs, _ABS)
self._compareCpu(x, np.negative, math_ops.negative)
self._compareCpu(x, np.negative, _NEG)
self._compareCpu(x, np.sign, math_ops.sign)

self._compareBothSparse(x, np.abs, math_ops.abs)
self._compareBothSparse(x, np.negative, math_ops.negative)
self._compareBothSparse(x, np.sign, math_ops.sign)
