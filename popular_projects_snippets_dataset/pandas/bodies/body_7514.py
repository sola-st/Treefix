# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_duplicates.py
mi = MultiIndex.from_arrays([[1, 2, 1, 2], [1, 1, 1, 2]], names=names)

res = mi.unique()
exp = MultiIndex.from_arrays([[1, 2, 2], [1, 1, 2]], names=mi.names)
tm.assert_index_equal(res, exp)

mi = MultiIndex.from_arrays([list("aaaa"), list("abab")], names=names)
res = mi.unique()
exp = MultiIndex.from_arrays([list("aa"), list("ab")], names=mi.names)
tm.assert_index_equal(res, exp)

mi = MultiIndex.from_arrays([list("aaaa"), list("aaaa")], names=names)
res = mi.unique()
exp = MultiIndex.from_arrays([["a"], ["a"]], names=mi.names)
tm.assert_index_equal(res, exp)

# GH #20568 - empty MI
mi = MultiIndex.from_arrays([[], []], names=names)
res = mi.unique()
tm.assert_index_equal(mi, res)
