# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list("ABC"))
s = Series([1, 2], mi)
backwards = s.iloc[[1, 0]]

result = s.sort_index(level="C", key=lambda x: -x)
tm.assert_series_equal(s, result)

result = s.sort_index(level="C", key=lambda x: x)  # nothing happens
tm.assert_series_equal(backwards, result)
