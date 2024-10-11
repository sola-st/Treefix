# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
result_y = np.array([p.get_y() for p in patches])
result_height = np.array([p.get_height() for p in patches])
result_x = np.array([p.get_x() for p in patches])
result_width = np.array([p.get_width() for p in patches])
# dtype is depending on above values, no need to check

if expected_y is not None:
    tm.assert_numpy_array_equal(result_y, expected_y, check_dtype=False)
if expected_h is not None:
    tm.assert_numpy_array_equal(result_height, expected_h, check_dtype=False)
if expected_x is not None:
    tm.assert_numpy_array_equal(result_x, expected_x, check_dtype=False)
if expected_w is not None:
    tm.assert_numpy_array_equal(result_width, expected_w, check_dtype=False)
