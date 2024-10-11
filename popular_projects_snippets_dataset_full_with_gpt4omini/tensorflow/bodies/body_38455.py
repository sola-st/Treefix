# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Create a 4D array of floats and reduce across some
# dimensions
np_arr = np.floor(np.arange(0.0, 210.0) / 100.0).reshape([2, 3, 5,
                                                          7]).astype(
                                                              np.float32)
self._compareAll(np_arr, None)
self._compareAll(np_arr, [])
self._compareAll(np_arr, [0])
self._compareAll(np_arr, [1])
self._compareAll(np_arr, [2])
self._compareAll(np_arr, [0, 1])
self._compareAll(np_arr, [1, 2])
# Need specialization for reduce(4D, [0, 2])
# self._compareAll(np_arr, [0, 2])
self._compareAll(np_arr, [0, 1, 2])
self._compareAll(np_arr, [1, 2, 3])
self._compareAll(np_arr, [0, 1, 2, 3])
