# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

index = IntervalIndex.from_arrays([0, 1], [1, 2], closed="right")

# __contains__ requires perfect matches to intervals.
assert 0 not in index
assert 1 not in index
assert 2 not in index

assert Interval(0, 1, closed="right") in index
assert Interval(0, 2, closed="right") not in index
assert Interval(0, 0.5, closed="right") not in index
assert Interval(3, 5, closed="right") not in index
assert Interval(-1, 0, closed="left") not in index
assert Interval(0, 1, closed="left") not in index
assert Interval(0, 1, closed="both") not in index
