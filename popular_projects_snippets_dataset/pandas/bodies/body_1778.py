# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
rng = date_range("2012-06-12", periods=200, freq="h").as_unit(unit)
ts = Series(np.random.randn(len(rng)), index=rng)

ts = ts.take(np.random.permutation(len(ts)))

result = ts.resample("D").sum()
exp = ts.sort_index().resample("D").sum()
tm.assert_series_equal(result, exp)
