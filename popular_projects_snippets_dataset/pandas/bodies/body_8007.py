# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
rng = Index(range(5))

result = Index(rng, dtype=dtype)
assert result.dtype == dtype

result = Index(range(5), dtype=dtype)
assert result.dtype == dtype
