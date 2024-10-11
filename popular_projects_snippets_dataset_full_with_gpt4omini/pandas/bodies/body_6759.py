# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
"""
        Interval specific tests for is_unique in addition to base class tests
        """
# unique overlapping - distinct endpoints
idx = IntervalIndex.from_tuples([(0, 1), (0.5, 1.5)], closed=closed)
assert idx.is_unique is True

# unique overlapping - shared endpoints
idx = IntervalIndex.from_tuples([(1, 2), (1, 3), (2, 3)], closed=closed)
assert idx.is_unique is True

# unique nested
idx = IntervalIndex.from_tuples([(-1, 1), (-2, 2)], closed=closed)
assert idx.is_unique is True

# unique NaN
idx = IntervalIndex.from_tuples([(np.NaN, np.NaN)], closed=closed)
assert idx.is_unique is True

# non-unique NaN
idx = IntervalIndex.from_tuples(
    [(np.NaN, np.NaN), (np.NaN, np.NaN)], closed=closed
)
assert idx.is_unique is False
