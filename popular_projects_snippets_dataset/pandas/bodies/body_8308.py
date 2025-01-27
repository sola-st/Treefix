# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# When taking the union of two DatetimeIndexes, we infer
#  a freq even if the arguments don't have freq.  This matches
#  TimedeltaIndex behavior.
dti = date_range("2016-01-01", periods=5)
left = dti[[0, 1, 3, 4]]
right = dti[[2, 3, 1]]

assert left.freq is None
assert right.freq is None

result = left.union(right)
tm.assert_index_equal(result, dti)
assert result.freq == "D"
