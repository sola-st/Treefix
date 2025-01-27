# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# https://github.com/pandas-dev/pandas/issues/36603
s = Series([1, 2, 3, 4, 5])
bins = Series([0, 2, 4, 6])
labels = Series(["a", "b", "c"])
result = cut(s, bins=bins, labels=labels, ordered=False)
expected = Series(["a", "a", "b", "b", "c"], dtype="category")
tm.assert_series_equal(result, expected)
