# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
equiv_pairs = [
    (RangeIndex(0, 9, 2), RangeIndex(0, 10, 2)),
    (RangeIndex(0), RangeIndex(1, -1, 3)),
    (RangeIndex(1, 2, 3), RangeIndex(1, 3, 4)),
    (RangeIndex(0, -9, -2), RangeIndex(0, -10, -2)),
]
for left, right in equiv_pairs:
    assert left.equals(right)
    assert right.equals(left)
