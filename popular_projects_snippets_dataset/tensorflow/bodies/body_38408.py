# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for rank in range(1, _MAX_RANK):
    # Avoid overflow by limiting array values.
    np_arr = self._makeIncremental((2,) * rank, dtypes.int64) % 11 + 1
    self._compareAllAxes(np_arr)
