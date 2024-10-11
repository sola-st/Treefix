# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index([1, 2, 3, 4], dtype=idx_dtype, name="foo")
taken = index.take([3, 0, 1])
assert index.name == taken.name
