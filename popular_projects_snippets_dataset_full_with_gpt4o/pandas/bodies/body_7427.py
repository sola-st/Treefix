# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
x = MultiIndex.from_tuples([("a", "b"), (1, 2), ("c", "d")], names=["x", "y"])
assert x[1:].names == x.names
