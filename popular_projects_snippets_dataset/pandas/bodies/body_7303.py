# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py

left = TimedeltaIndex(["1 day 15:19:49.695000"])
right = TimedeltaIndex(
    ["2 day 13:04:21.322000", "1 day 15:27:24.873000", "1 day 15:31:05.350000"]
)

result = left.union(right)
exp = TimedeltaIndex(sorted(set(left) | set(right)))
tm.assert_index_equal(result, exp)
