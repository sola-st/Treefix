# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
arr = np.tile(np.arange(0, 1.01, 0.1), 4)

result, bins = cut(arr, 4, retbins=True, right=right)
ex_levels = IntervalIndex.from_breaks(breaks, closed=closed)
tm.assert_index_equal(result.categories, ex_levels)
