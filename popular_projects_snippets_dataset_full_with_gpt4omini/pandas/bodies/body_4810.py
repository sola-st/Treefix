# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["a", "b", np.nan, "c", np.nan, "eeeeee"], dtype=any_string_dtype)

result = s.str.center(5)
expected = Series(
    ["  a  ", "  b  ", np.nan, "  c  ", np.nan, "eeeeee"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)

result = s.str.ljust(5)
expected = Series(
    ["a    ", "b    ", np.nan, "c    ", np.nan, "eeeeee"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)

result = s.str.rjust(5)
expected = Series(
    ["    a", "    b", np.nan, "    c", np.nan, "eeeeee"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)
