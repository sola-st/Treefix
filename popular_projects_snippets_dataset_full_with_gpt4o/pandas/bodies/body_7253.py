# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index(range(6))
result = index.get_slice_bound(bound, side=side)
assert result == expected
