# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for rank in range(1, _MAX_RANK + 1):
    np_arr = self._makeIncremental((2,) * rank, dtypes.float32)
    self._compareAllAxes(np_arr)
