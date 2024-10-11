# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# #1327
rng = date_range("1/1/2000", freq="B", periods=20).as_unit(unit)
ts = Series(np.random.randn(len(rng)), index=rng)

resampled = ts.resample("W").mean()
expected = ts.resample("W-SUN").mean()
tm.assert_series_equal(resampled, expected)
