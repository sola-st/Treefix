# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_indexing.py
index = RangeIndex(1, 5, name="foo")
taken = index.take([3, 0, 1])
assert index.name == taken.name
