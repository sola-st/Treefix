# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
res = Series([pd.NaT, pd.NaT]).quantile(0.5)
assert res is pd.NaT

res = Series([pd.NaT, pd.NaT]).quantile([0.5])
tm.assert_series_equal(res, Series([pd.NaT], index=[0.5]))
