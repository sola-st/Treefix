# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["foo", "b", "ba"], dtype=any_string_dtype)
result = ser.str[1]
expected = Series(["o", np.nan, "a"], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
