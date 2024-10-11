# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np_arr = self._makeRandom((2**7,), dtypes.int8)
self._compareAllAxes(np_arr)
