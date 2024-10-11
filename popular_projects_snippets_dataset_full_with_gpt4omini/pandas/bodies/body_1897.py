# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH12774
series = Series(1, index=period_range(start="2000", periods=100))
result = series.resample(freq).count()
expected_index = period_range(
    start="2000", freq=freq, periods=len(expected_vals)
)
expected = Series(expected_vals, index=expected_index)
tm.assert_series_equal(result, expected)
