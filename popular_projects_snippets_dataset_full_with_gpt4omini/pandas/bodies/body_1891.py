# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/1990", "6/30/1995", freq="M")
result = ts.resample("a-dec").mean()

resampled = result.resample(freq, convention="end").ffill()
expected = result.to_timestamp(freq, how="end")
expected = expected.asfreq(freq, "ffill").to_period(freq)
tm.assert_series_equal(resampled, expected)
