# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for dtype in [np.float32, np.float64]:
    np_arr = np.array([-1.]).astype(dtype)
    self._compareAll(np_arr, None)
