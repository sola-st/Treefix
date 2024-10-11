# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["a", "b", np.nan, "c", np.nan, "d"], dtype=any_string_dtype)

result = ser.str.repeat(3)
expected = Series(
    ["aaa", "bbb", np.nan, "ccc", np.nan, "ddd"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)

result = ser.str.repeat([1, 2, 3, 4, 5, 6])
expected = Series(
    ["a", "bb", np.nan, "cccc", np.nan, "dddddd"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)
