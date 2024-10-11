# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
ser = pd.Series([False, True, np.nan, False])
result = getattr(ser, method)()
tm.assert_series_equal(result, expected)
