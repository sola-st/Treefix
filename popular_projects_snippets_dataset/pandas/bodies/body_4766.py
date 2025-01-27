# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["ab", "a b c", "bc"], dtype=any_string_dtype)
result = ser.str.removesuffix(suffix)
ser_expected = Series(expected, dtype=any_string_dtype)
tm.assert_series_equal(result, ser_expected)
