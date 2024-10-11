# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index(np.array([10, 12, 12, 14], dtype=dtype))
assert index.slice_locs(12, 12) == (1, 3)
assert index.slice_locs(11, 13) == (1, 3)

index2 = index[::-1]
assert index2.slice_locs(12, 12) == (1, 3)
assert index2.slice_locs(13, 11) == (1, 3)
