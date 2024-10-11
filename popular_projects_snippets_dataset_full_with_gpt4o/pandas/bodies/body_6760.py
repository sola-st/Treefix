# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# increasing non-overlapping
idx = IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)], closed=closed)
assert idx.is_monotonic_increasing is True
assert idx._is_strictly_monotonic_increasing is True
assert idx.is_monotonic_decreasing is False
assert idx._is_strictly_monotonic_decreasing is False

# decreasing non-overlapping
idx = IntervalIndex.from_tuples([(4, 5), (2, 3), (1, 2)], closed=closed)
assert idx.is_monotonic_increasing is False
assert idx._is_strictly_monotonic_increasing is False
assert idx.is_monotonic_decreasing is True
assert idx._is_strictly_monotonic_decreasing is True

# unordered non-overlapping
idx = IntervalIndex.from_tuples([(0, 1), (4, 5), (2, 3)], closed=closed)
assert idx.is_monotonic_increasing is False
assert idx._is_strictly_monotonic_increasing is False
assert idx.is_monotonic_decreasing is False
assert idx._is_strictly_monotonic_decreasing is False

# increasing overlapping
idx = IntervalIndex.from_tuples([(0, 2), (0.5, 2.5), (1, 3)], closed=closed)
assert idx.is_monotonic_increasing is True
assert idx._is_strictly_monotonic_increasing is True
assert idx.is_monotonic_decreasing is False
assert idx._is_strictly_monotonic_decreasing is False

# decreasing overlapping
idx = IntervalIndex.from_tuples([(1, 3), (0.5, 2.5), (0, 2)], closed=closed)
assert idx.is_monotonic_increasing is False
assert idx._is_strictly_monotonic_increasing is False
assert idx.is_monotonic_decreasing is True
assert idx._is_strictly_monotonic_decreasing is True

# unordered overlapping
idx = IntervalIndex.from_tuples([(0.5, 2.5), (0, 2), (1, 3)], closed=closed)
assert idx.is_monotonic_increasing is False
assert idx._is_strictly_monotonic_increasing is False
assert idx.is_monotonic_decreasing is False
assert idx._is_strictly_monotonic_decreasing is False

# increasing overlapping shared endpoints
idx = IntervalIndex.from_tuples([(1, 2), (1, 3), (2, 3)], closed=closed)
assert idx.is_monotonic_increasing is True
assert idx._is_strictly_monotonic_increasing is True
assert idx.is_monotonic_decreasing is False
assert idx._is_strictly_monotonic_decreasing is False

# decreasing overlapping shared endpoints
idx = IntervalIndex.from_tuples([(2, 3), (1, 3), (1, 2)], closed=closed)
assert idx.is_monotonic_increasing is False
assert idx._is_strictly_monotonic_increasing is False
assert idx.is_monotonic_decreasing is True
assert idx._is_strictly_monotonic_decreasing is True

# stationary
idx = IntervalIndex.from_tuples([(0, 1), (0, 1)], closed=closed)
assert idx.is_monotonic_increasing is True
assert idx._is_strictly_monotonic_increasing is False
assert idx.is_monotonic_decreasing is True
assert idx._is_strictly_monotonic_decreasing is False

# empty
idx = IntervalIndex([], closed=closed)
assert idx.is_monotonic_increasing is True
assert idx._is_strictly_monotonic_increasing is True
assert idx.is_monotonic_decreasing is True
assert idx._is_strictly_monotonic_decreasing is True
