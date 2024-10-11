# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# GH 24471 Test intersection outcome given the sort keyword
# for equal indices intersection should return the original index
first = timedelta_range("1 day", periods=4, freq="h")
second = timedelta_range("1 day", periods=4, freq="h")
intersect = first.intersection(second, sort=sort)
if sort is None:
    tm.assert_index_equal(intersect, second.sort_values())
assert tm.equalContents(intersect, second)

# Corner cases
inter = first.intersection(first, sort=sort)
assert inter is first
