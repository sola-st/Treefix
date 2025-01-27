# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH#41831
index = IntervalIndex([np.nan, np.nan])

assert not index.is_monotonic_increasing
assert not index._is_strictly_monotonic_increasing
assert not index.is_monotonic_increasing
assert not index._is_strictly_monotonic_decreasing
assert not index.is_monotonic_decreasing
