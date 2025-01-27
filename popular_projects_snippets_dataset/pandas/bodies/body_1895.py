# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/1990", "12/31/1995", freq="M")
result = ts.resample(target, convention=convention).ffill()
expected = result.to_timestamp(target, how=convention)
expected = expected.asfreq(target, "ffill").to_period()
tm.assert_series_equal(result, expected)
