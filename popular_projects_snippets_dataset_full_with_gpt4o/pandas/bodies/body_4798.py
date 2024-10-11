# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["a", np.nan, "b", True, datetime.today(), "foo", None, 1, 2.0])

result = s.str.upper()
expected = Series(["A", np.nan, "B", np.nan, np.nan, "FOO", np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)

result = s.str.lower()
expected = Series(["a", np.nan, "b", np.nan, np.nan, "foo", np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)
