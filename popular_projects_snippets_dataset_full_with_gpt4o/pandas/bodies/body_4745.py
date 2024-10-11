# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# GH: 31632
ser = Series(["a", arg], dtype=any_string_dtype)
result = ser.str.repeat([3, repeat])
expected = Series(["aaa", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
