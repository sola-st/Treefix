# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
result = MultiIndex.from_tuples(idx)
assert (result.values == idx.values).all()
