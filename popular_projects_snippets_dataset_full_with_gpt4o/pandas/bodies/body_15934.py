# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list("ABC"))
s = Series([1, 2], mi)
backwards = s.iloc[[1, 0]]

res = s.sort_index(level="A")
tm.assert_series_equal(backwards, res)

res = s.sort_index(level=["A", "B"])
tm.assert_series_equal(backwards, res)

res = s.sort_index(level="A", sort_remaining=False)
tm.assert_series_equal(s, res)

res = s.sort_index(level=["A", "B"], sort_remaining=False)
tm.assert_series_equal(s, res)
