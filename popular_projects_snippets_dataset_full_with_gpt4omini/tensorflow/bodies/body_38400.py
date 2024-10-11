# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for rank in range(1, _MAX_RANK + 1):
    np_arr = self._makeIncremental((2,) * rank, dtype)
    rtol, atol = (1e-2, 5e-1) if dtype == dtypes.bfloat16 else (1e-6, 1e-6)
    self._compareAllAxes(np_arr, rtol=rtol, atol=atol)
