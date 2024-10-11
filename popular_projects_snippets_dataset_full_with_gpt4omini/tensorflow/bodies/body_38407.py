# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Numpy automatically upgrades the type of np.prod from int32 to int64, so
# Numpy does not overflow an int32 np.prod while TensorFlow does. To avoid
# overflow, limit array values.
for rank in range(1, _MAX_RANK):
    np_arr = self._makeIncremental((2,) * rank, dtypes.int32) % 5 + 1
    self._compareAllAxes(np_arr)
