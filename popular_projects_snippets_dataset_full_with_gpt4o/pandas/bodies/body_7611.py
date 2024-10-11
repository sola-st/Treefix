# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH 18485 : NaN in MultiIndex
levels = [["a", "b"], ["c", "d"]]
key = ["b", "d"]
levels[level] = np.array([0, nulls_fixture], dtype=type(nulls_fixture))
key[level] = nulls_fixture
idx = MultiIndex.from_product(levels)
assert idx.get_loc(tuple(key)) == 3
