# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
start, end = Timestamp("20180101", tz=tz), Timestamp("20181231", tz=tz)
breaks = date_range(start=start, end=end, freq=freq)
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
if not breaks.freq.is_anchored() and tz is None:
    # matches expected only for non-anchored offsets and tz naive
    # (anchored/DST transitions cause unequal spacing in expected)
    result = interval_range(
        start=start, end=end, periods=periods, name=name, closed=closed
    )
    tm.assert_index_equal(result, expected)
