# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
idx = period_range("20010101", periods=10, freq="D", name="bob")
assert idx.name == idx[1:].name
