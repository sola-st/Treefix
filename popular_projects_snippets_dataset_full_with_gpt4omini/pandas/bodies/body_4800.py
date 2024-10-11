# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["FOO", np.nan, "bar", True, datetime.today(), "blah", None, 1, 2.0])
result = s.str.capitalize()
expected = Series(
    ["Foo", np.nan, "Bar", np.nan, np.nan, "Blah", np.nan, np.nan, np.nan]
)
tm.assert_series_equal(result, expected)
