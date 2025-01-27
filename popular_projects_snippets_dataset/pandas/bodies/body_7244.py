# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH#35788 should return False, not raise TypeError
index = Index([0, 1, 2, 3, 4], dtype=dtype)
assert None not in index
