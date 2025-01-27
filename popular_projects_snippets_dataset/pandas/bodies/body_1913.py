# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/2000", "2/1/2000", freq="B")

result = ts.resample("D").asfreq()
expected = ts.asfreq("D").reindex(period_range("1/3/2000", "2/1/2000"))
tm.assert_series_equal(result, expected)

ts = simple_period_range_series("1/1/2000", "2/1/2000")
result = ts.resample("H", convention="s").asfreq()
exp_rng = period_range("1/1/2000", "2/1/2000 23:00", freq="H")
expected = ts.asfreq("H", how="s").reindex(exp_rng)
tm.assert_series_equal(result, expected)
