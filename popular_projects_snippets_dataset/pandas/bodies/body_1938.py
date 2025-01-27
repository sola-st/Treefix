# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py

# GH 12072
index = timedelta_range("0", periods=9, freq="10L")
series = Series(range(9), index=index)
result = series.resample("10L").mean()
expected = series.astype(float)
tm.assert_series_equal(result, expected)
