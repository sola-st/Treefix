# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 23563: consistent closed results in interval dtype
data = [Interval(0, 1), Interval(0, 2), None]
result = Series(data_constructor(data))
expected = Series(IntervalArray(data))
assert result.dtype == "interval[float64, right]"
tm.assert_series_equal(result, expected)
