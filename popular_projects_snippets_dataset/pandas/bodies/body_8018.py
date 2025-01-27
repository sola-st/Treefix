# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
index = Index(vals, dtype="category")
assert isinstance(index, CategoricalIndex)
