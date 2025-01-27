# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["aafootwo", "aabartwo", np.nan, "aabazqux"], dtype=any_string_dtype)
result = ser.str.slice(start, stop, step)
expected = Series(expected, dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
