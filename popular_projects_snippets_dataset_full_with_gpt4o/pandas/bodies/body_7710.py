# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_isin.py
# GH 19132
midx = MultiIndex.from_arrays([[np.nan, "a", "b"], ["c", "d", np.nan]])
result = midx.isin(labels, level=level)
tm.assert_numpy_array_equal(result, expected)
