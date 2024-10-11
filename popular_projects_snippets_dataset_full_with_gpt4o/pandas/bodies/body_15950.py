# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
s = Series([1, 2, 3], DatetimeIndex(["2008-10-24", "2008-11-23", "2007-12-22"]))

result = s.sort_index(key=lambda x: x.month)
expected = s.iloc[[0, 1, 2]]
tm.assert_series_equal(result, expected)

result = s.sort_index(key=lambda x: x.day)
expected = s.iloc[[2, 1, 0]]
tm.assert_series_equal(result, expected)

result = s.sort_index(key=lambda x: x.year)
expected = s.iloc[[2, 0, 1]]
tm.assert_series_equal(result, expected)

result = s.sort_index(key=lambda x: x.month_name())
expected = s.iloc[[2, 1, 0]]
tm.assert_series_equal(result, expected)
