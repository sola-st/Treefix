# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py
# GH 28697
s = Series([1, 2, 1, 3], ["first", "b", "second", "c"])
result = s.sort_values(ascending=False, kind="mergesort")
expected = Series([3, 2, 1, 1], ["c", "b", "first", "second"])
tm.assert_series_equal(result, expected)
