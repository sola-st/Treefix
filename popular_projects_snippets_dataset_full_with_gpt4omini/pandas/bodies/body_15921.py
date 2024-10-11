# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py

# floats
s = Series([], dtype="float64")

res = s.quantile(0.5)
assert np.isnan(res)

res = s.quantile([0.5])
exp = Series([np.nan], index=[0.5])
tm.assert_series_equal(res, exp)

# int
s = Series([], dtype="int64")

res = s.quantile(0.5)
assert np.isnan(res)

res = s.quantile([0.5])
exp = Series([np.nan], index=[0.5])
tm.assert_series_equal(res, exp)

# datetime
s = Series([], dtype="datetime64[ns]")

res = s.quantile(0.5)
assert res is pd.NaT

res = s.quantile([0.5])
exp = Series([pd.NaT], index=[0.5])
tm.assert_series_equal(res, exp)
