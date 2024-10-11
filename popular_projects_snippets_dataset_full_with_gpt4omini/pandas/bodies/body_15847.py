# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 11792: Test with replacing NaT in a list with tz data
ts = pd.Timestamp("2015/01/01", tz="UTC")
s = pd.Series([pd.NaT, pd.Timestamp("2015/01/01", tz="UTC")])
result = s.replace([np.nan, pd.NaT], pd.Timestamp.min)
expected = pd.Series([pd.Timestamp.min, ts], dtype=object)
tm.assert_series_equal(expected, result)
