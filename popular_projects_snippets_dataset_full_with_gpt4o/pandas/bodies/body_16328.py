# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# construction from interval & array of intervals
intervals = interval_constructor.from_breaks(np.arange(3), closed="right")
result = Series(intervals)
assert result.dtype == "interval[int64, right]"
tm.assert_index_equal(Index(result.values), Index(intervals))
