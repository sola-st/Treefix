# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
# GH 20976: linspace behavior defined from start/end/periods
# accounts for the hour gained/lost during DST transition
result = interval_range(start=start, end=end, periods=2)
expected = IntervalIndex.from_breaks([start, mid, end])
tm.assert_index_equal(result, expected)
