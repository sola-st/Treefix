# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
rng = period_range("2000Q1", periods=10, freq="Q-DEC")
ts = Series(np.arange(10), index=rng)

result = ts.resample("A").mean()
exp = ts.to_timestamp().resample("A").mean().to_period()
tm.assert_series_equal(result, exp)
