# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
s = [2, 3, 4, 2]
x = self._makeIncremental(s, dtypes.float32) / 20.
# No zeros in input
self._compareGradientAxes(x, rtol=1e-3, atol=1e-3)
# Zero at beginning
x1 = x.copy()
x1[:, :, 0, :] = 0
self._compareGradientAxes(x1, rtol=1e-3, atol=1e-3)
# Zero at end
x2 = x.copy()
x2[:, :, -1, :] = 0
self._compareGradientAxes(x2, rtol=1e-3, atol=1e-3)
# Zero in middle
x3 = x.copy()
x3[:, :, 2, :] = 0
self._compareGradientAxes(x3, rtol=1e-3, atol=1e-3)
# All zeros
x4 = x.copy()
x4[:, :, :, :] = 0
self._compareGradientAxes(x4, rtol=1e-3, atol=1e-3)
