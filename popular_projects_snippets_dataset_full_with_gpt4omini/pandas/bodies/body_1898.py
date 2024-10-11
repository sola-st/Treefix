# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py

# GH12770
series = Series(range(3), index=period_range(start="2000", periods=3, freq="M"))
expected = series

result = getattr(series.resample("M"), resample_method)()
tm.assert_series_equal(result, expected)
