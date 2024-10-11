# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["a", "b", np.nan, "c", np.nan, "eeeeee"], dtype=any_string_dtype)

result = s.str.pad(5, side="left")
expected = Series(
    ["    a", "    b", np.nan, "    c", np.nan, "eeeeee"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)

result = s.str.pad(5, side="right")
expected = Series(
    ["a    ", "b    ", np.nan, "c    ", np.nan, "eeeeee"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)

result = s.str.pad(5, side="both")
expected = Series(
    ["  a  ", "  b  ", np.nan, "  c  ", np.nan, "eeeeee"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)
