# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index([np.nan, 1, 2])
assert index.slice_locs(1) == (1, 3)
assert index.slice_locs(np.nan) == (0, 3)

index = Index([0, np.nan, np.nan, 1, 2])
assert index.slice_locs(np.nan) == (1, 5)
