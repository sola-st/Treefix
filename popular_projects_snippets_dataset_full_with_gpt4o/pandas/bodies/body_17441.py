# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
off = _create_offset(offset_types)

expected = np.array([[off, off * 2], [off * 3, off * 4]])

result = np.array([[1, 2], [3, 4]]) * off
tm.assert_numpy_array_equal(result, expected)

result = off * np.array([[1, 2], [3, 4]])
tm.assert_numpy_array_equal(result, expected)
