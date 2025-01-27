# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# GH 23705
ci = CategoricalIndex(IntervalIndex.from_breaks(range(3)))
result = item in ci
assert result is expected
