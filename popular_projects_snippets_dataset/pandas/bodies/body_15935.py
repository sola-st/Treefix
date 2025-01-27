# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py

mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list("ABC"))
s = Series([1, 2], mi)
backwards = s.iloc[[1, 0]]

# implicit sort_remaining=True
res = s.sort_index(level=level)
tm.assert_series_equal(backwards, res)

# GH#13496
# sort has no effect without remaining lvls
res = s.sort_index(level=level, sort_remaining=False)
tm.assert_series_equal(s, res)
