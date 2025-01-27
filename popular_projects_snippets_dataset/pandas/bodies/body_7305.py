# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# When taking the union of two TimedeltaIndexes, we infer
#  a freq even if the arguments don't have freq.  This matches
#  DatetimeIndex behavior.
tdi = timedelta_range("1 Day", periods=5)
left = tdi[[0, 1, 3, 4]]
right = tdi[[2, 3, 1]]

assert left.freq is None
assert right.freq is None

result = left.union(right)
tm.assert_index_equal(result, tdi)
assert result.freq == "D"
