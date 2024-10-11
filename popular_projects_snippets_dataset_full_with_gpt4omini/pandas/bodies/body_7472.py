# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#38423
mi = MultiIndex.from_arrays([[]])
mi2 = MultiIndex.from_arrays([[1, 2], [3, 4]], names=["a", "b"])
result = mi.union(mi2)
expected = MultiIndex.from_arrays([[1, 2], [3, 4]])
tm.assert_index_equal(result, expected)
