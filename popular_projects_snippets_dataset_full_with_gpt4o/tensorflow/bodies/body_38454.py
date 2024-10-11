# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Create a 1D array of floats
np_arr = np.asarray([0.0, 1.0, -1.0, 0.0, 0.0, 3.0]).astype(np.float32)
self._compareAll(np_arr, [0])
