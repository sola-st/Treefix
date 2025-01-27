# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
rng = date_range("1/1/2000", periods=10, freq="W-WED")
ts = Series(np.random.randn(len(rng)), index=rng)

result = ts.resample("W-THU").asfreq()

assert result.isna().all()

result = ts.resample("W-THU").asfreq().ffill()[:-1]
expected = ts.asfreq("W-THU").ffill()
tm.assert_series_equal(result, expected)
