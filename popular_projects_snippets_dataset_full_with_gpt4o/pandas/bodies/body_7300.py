# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
tdi = timedelta_range("1day", periods=5)

left = tdi[3:]
right = tdi[:3]

# Check that we are testing the desired code path
assert left._can_fast_union(right)

result = left.union(right)
tm.assert_index_equal(result, tdi)

result = left.union(right, sort=False)
expected = TimedeltaIndex(["4 Days", "5 Days", "1 Days", "2 Day", "3 Days"])
tm.assert_index_equal(result, expected)
