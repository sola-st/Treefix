# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = RangeIndex(1, 2, name="asdf")
assert idx.name == idx[1:].name
