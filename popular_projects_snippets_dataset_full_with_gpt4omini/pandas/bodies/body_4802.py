# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["FOO", np.nan, "bar", True, datetime.today(), "Blah", None, 1, 2.0])
result = s.str.swapcase()
expected = Series(
    ["foo", np.nan, "BAR", np.nan, np.nan, "bLAH", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)
