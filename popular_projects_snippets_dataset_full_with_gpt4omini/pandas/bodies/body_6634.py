# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = simple_index
assert idx.all() == idx.values.all()
assert idx.any() == idx.values.any()
