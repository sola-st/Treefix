# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
rng = period_range("1/1/2000", "1/5/2000", freq="T")
ts = Series(np.random.randn(len(rng)), index=rng)
expected = ts.to_timestamp().resample(freq).mean()
if kind != "timestamp":
    expected = expected.to_period(freq)
result = ts.resample(freq, kind=kind).mean()
tm.assert_series_equal(result, expected)
