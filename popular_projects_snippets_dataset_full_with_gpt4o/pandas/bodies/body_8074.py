# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = simple_index
assert getattr(index, op)() == getattr(index.values, op)()
