# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
# GH 21161
if freq is None:
    breaks = [0.5, 1.5, 2.5, 3.5, 4.5]
else:
    breaks = [0.5, 2.0, 3.5, 5.0, 6.5]
expected = IntervalIndex.from_breaks(breaks)

result = interval_range(start=start, end=end, periods=4, freq=freq)
tm.assert_index_equal(result, expected)
