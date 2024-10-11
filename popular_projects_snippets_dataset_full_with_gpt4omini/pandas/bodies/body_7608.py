# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH 18520
levels = [np.array([0, 1]).astype(dtype1), np.array([0, 1]).astype(dtype2)]
idx = MultiIndex.from_product(levels)
assert idx.get_loc(idx[2]) == 2
