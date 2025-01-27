# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
taken = idx.take([3, 0, 1])
assert taken.names == idx.names
