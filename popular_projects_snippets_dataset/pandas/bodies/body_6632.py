# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
index = RangeIndex(0, 20, 2)
assert index.is_monotonic_increasing is True
assert index.is_monotonic_increasing is True
assert index.is_monotonic_decreasing is False
assert index._is_strictly_monotonic_increasing is True
assert index._is_strictly_monotonic_decreasing is False

index = RangeIndex(4, 0, -1)
assert index.is_monotonic_increasing is False
assert index._is_strictly_monotonic_increasing is False
assert index.is_monotonic_decreasing is True
assert index._is_strictly_monotonic_decreasing is True

index = RangeIndex(1, 2)
assert index.is_monotonic_increasing is True
assert index.is_monotonic_increasing is True
assert index.is_monotonic_decreasing is True
assert index._is_strictly_monotonic_increasing is True
assert index._is_strictly_monotonic_decreasing is True

index = RangeIndex(2, 1)
assert index.is_monotonic_increasing is True
assert index.is_monotonic_increasing is True
assert index.is_monotonic_decreasing is True
assert index._is_strictly_monotonic_increasing is True
assert index._is_strictly_monotonic_decreasing is True

index = RangeIndex(1, 1)
assert index.is_monotonic_increasing is True
assert index.is_monotonic_increasing is True
assert index.is_monotonic_decreasing is True
assert index._is_strictly_monotonic_increasing is True
assert index._is_strictly_monotonic_decreasing is True
