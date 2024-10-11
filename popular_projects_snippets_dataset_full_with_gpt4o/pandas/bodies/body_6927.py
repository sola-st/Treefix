# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_indexing.py
index = Index(data)
result = index.get_slice_bound(bound, side=side)
assert result == expected
