# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# Should be True in all cases
tpls = [(0, 1), (2, 3), (4, 5), (6, 7)]
idx = IntervalIndex.from_tuples(tpls, closed=closed)
assert idx.is_non_overlapping_monotonic is True

idx = IntervalIndex.from_tuples(tpls[::-1], closed=closed)
assert idx.is_non_overlapping_monotonic is True

# Should be False in all cases (overlapping)
tpls = [(0, 2), (1, 3), (4, 5), (6, 7)]
idx = IntervalIndex.from_tuples(tpls, closed=closed)
assert idx.is_non_overlapping_monotonic is False

idx = IntervalIndex.from_tuples(tpls[::-1], closed=closed)
assert idx.is_non_overlapping_monotonic is False

# Should be False in all cases (non-monotonic)
tpls = [(0, 1), (2, 3), (6, 7), (4, 5)]
idx = IntervalIndex.from_tuples(tpls, closed=closed)
assert idx.is_non_overlapping_monotonic is False

idx = IntervalIndex.from_tuples(tpls[::-1], closed=closed)
assert idx.is_non_overlapping_monotonic is False

# Should be False for closed='both', otherwise True (GH16560)
if closed == "both":
    idx = IntervalIndex.from_breaks(range(4), closed=closed)
    assert idx.is_non_overlapping_monotonic is False
else:
    idx = IntervalIndex.from_breaks(range(4), closed=closed)
    assert idx.is_non_overlapping_monotonic is True
