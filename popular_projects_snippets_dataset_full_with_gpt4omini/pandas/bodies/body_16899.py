# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# see gh-15431
ser = Series([data] * length)
result = qcut(ser, 1, labels=labels)

if labels is None:
    intervals = IntervalIndex([Interval(start, end)] * length, closed="right")
    expected = Series(intervals).astype(CDT(ordered=True))
else:
    expected = Series([0] * length, dtype=np.intp)

tm.assert_series_equal(result, expected)
