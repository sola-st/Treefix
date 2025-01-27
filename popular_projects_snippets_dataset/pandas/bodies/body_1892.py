# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
rng = period_range("1/1/2000", periods=5, freq="A")
ts = Series(np.random.randn(len(rng)), rng)

result = ts.resample("M", convention="end").ffill(limit=2)
expected = ts.asfreq("M").reindex(result.index, method="ffill", limit=2)
tm.assert_series_equal(result, expected)
