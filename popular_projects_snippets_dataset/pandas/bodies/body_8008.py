# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
cat = Categorical([1, 2, 3])

result = Index(cat, dtype=dtype)
assert result.dtype == dtype
