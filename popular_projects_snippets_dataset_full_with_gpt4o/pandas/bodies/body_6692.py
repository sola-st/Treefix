# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
start, end = 0, 100
breaks = np.arange(101, step=freq)
expected = IntervalIndex.from_breaks(breaks, name=name, closed=closed)

# defined from start/end/freq
result = interval_range(
    start=start, end=end, freq=freq, name=name, closed=closed
)
tm.assert_index_equal(result, expected)

# defined from start/periods/freq
result = interval_range(
    start=start, periods=periods, freq=freq, name=name, closed=closed
)
tm.assert_index_equal(result, expected)

# defined from end/periods/freq
result = interval_range(
    end=end, periods=periods, freq=freq, name=name, closed=closed
)
tm.assert_index_equal(result, expected)

# GH 20976: linspace behavior defined from start/end/periods
result = interval_range(
    start=start, end=end, periods=periods, name=name, closed=closed
)
tm.assert_index_equal(result, expected)
