# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 15036
s = Series([1, 2, 3], [np.nan, np.nan, np.nan])
result = s.groupby(s.index).sum()
expected = Series([], index=Index([], dtype=np.float64), dtype=np.int64)
tm.assert_series_equal(result, expected)
