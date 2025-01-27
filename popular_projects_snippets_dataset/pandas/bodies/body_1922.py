# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
rng = period_range("2000-01", periods=3, freq="M")
ts = Series(np.arange(3), index=rng)

# hacky way to get same thing
exp_index = period_range("2000-01-01", "2000-03-31", freq="D")
expected = ts.asfreq("D", how="end").reindex(exp_index)
expected = expected.fillna(method="bfill")

result = ts.resample("D").mean()

tm.assert_series_equal(result, expected)
