# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["  aa  ", np.nan, " bb \t\n", True, datetime.today(), None, 1, 2.0])

result = getattr(ser.str, method)()
expected = Series(exp + [np.nan, np.nan, np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)
