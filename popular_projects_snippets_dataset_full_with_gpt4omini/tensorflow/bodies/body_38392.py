# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
s = [2, 3, 4, 2]
for dtype in [dtypes.float32, dtypes.float64]:
    x = self._makeIncremental(s, dtype)
    self._compareGradientAxes(x, rtol=1e-3, atol=1e-3)
