# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#41234
mi = MultiIndex.from_arrays([[1, 2], [3, 4]], names=["a", "b"])
ri = pd.RangeIndex(0)

result_left = mi.union(ri)
tm.assert_index_equal(mi, result_left, check_names=False)

result_right = ri.union(mi)
tm.assert_index_equal(mi, result_right, check_names=False)
