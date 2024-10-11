# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series([(1, 2), (1,), (3, 4, 5)])
result = ser.str[1]
expected = Series([2, np.nan, 4])
tm.assert_series_equal(result, expected)
