# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
box = box_with_array
ser = Series([1, 2, 3], dtype=dtype)
expected = Series([np.nan, np.nan, np.nan], dtype=dtype)

ser = tm.box_expected(ser, box)
expected = tm.box_expected(expected, box)

result = np.nan + ser
tm.assert_equal(result, expected)

result = ser + np.nan
tm.assert_equal(result, expected)
