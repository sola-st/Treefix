# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
idx = simple_index
assert idx.all() == idx.values.all()
assert idx.any() == idx.values.any()
