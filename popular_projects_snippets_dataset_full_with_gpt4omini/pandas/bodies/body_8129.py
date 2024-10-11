# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = simple_index
assert index.all() == index.values.all()
assert index.any() == index.values.any()
