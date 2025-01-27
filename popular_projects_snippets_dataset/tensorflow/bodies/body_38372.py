# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for dtype in [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]:
    x = self._makeIncremental([2, 3, 4, 2], dtype)
    self._compareGradientAxes(x)
