# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np_arr = self._makeRandom((2**15,), dtypes.int16)
self._compareAllAxes(np_arr)
