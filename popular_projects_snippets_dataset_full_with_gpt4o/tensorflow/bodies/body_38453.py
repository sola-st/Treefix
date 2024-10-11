# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Create a 1D array of floats
np_arr = np.asarray([False, False, True, False, False, True])
self._compareAll(np_arr, None)
self._compareAll(np_arr, [])
self._compareAll(np_arr, [0])
