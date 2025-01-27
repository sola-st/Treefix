# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index([1.0, 2.0, np.nan], dtype=np.float64)
assert 1.0 in index
