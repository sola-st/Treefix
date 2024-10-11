# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for dtype in [np.float32, np.float64]:
    for special_value_x in [-np.inf, np.inf]:
        for special_value_y in [-np.inf, np.inf]:
            np_arr = np.array([special_value_x, special_value_y]).astype(dtype)
            self._compareAll(np_arr, None)
