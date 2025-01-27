# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Create a 3D array of floats and reduce across all possible
# dimensions
np_arr = np.arange(1, 31).reshape([2, 3, 5]).astype(np.float32)
self._compareAll(np_arr, None)
self._compareAll(np_arr, [])
self._compareAll(np_arr, [0])
self._compareAll(np_arr, [1])
self._compareAll(np_arr, [2])
self._compareAll(np_arr, [0, 1])
self._compareAll(np_arr, [1, 2])
self._compareAll(np_arr, [0, 2])
self._compareAll(np_arr, [0, 1, 2])
