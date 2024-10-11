# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH 18818, GH 15994 : as flat index, cast int to float and vice-versa
levels = [["a", "b"], ["c", "d"]]
key = ["b", "d"]
lev_dtype, key_dtype = dtypes
levels[level] = np.array([0, 1], dtype=lev_dtype)
key[level] = key_dtype(1)
idx = MultiIndex.from_product(levels)
assert idx.get_loc(tuple(key)) == 3
