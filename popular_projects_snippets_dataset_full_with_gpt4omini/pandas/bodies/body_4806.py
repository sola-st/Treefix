# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["a", np.nan, "b", True, datetime.today(), "ee", None, 1, 2.0])

result = s.str.pad(5, side="left")
expected = Series(
    ["    a", np.nan, "    b", np.nan, np.nan, "   ee", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)

result = s.str.pad(5, side="right")
expected = Series(
    ["a    ", np.nan, "b    ", np.nan, np.nan, "ee   ", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)

result = s.str.pad(5, side="both")
expected = Series(
    ["  a  ", np.nan, "  b  ", np.nan, np.nan, "  ee ", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)
