# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/1990", "6/30/1995", freq="M")
result = ts.resample("a-dec").mean()

expected = ts.groupby(ts.index.year).mean()
expected.index = period_range("1/1/1990", "6/30/1995", freq="a-dec")
tm.assert_series_equal(result, expected)

# this is ok
tm.assert_series_equal(ts.resample("a-dec").mean(), result)
tm.assert_series_equal(ts.resample("a").mean(), result)
