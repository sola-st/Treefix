# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_indexing.py
index = Index(list("abcdef"))
result = index.get_slice_bound("e", side=side)
assert result == expected
