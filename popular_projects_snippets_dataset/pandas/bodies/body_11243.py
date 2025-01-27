# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 42731
obj = frame_or_series([1, 2, 3, 4], index=index)
groups = Series([1, 0, 1, 0], index=index, name=("a", "a"))
result = obj.groupby(groups).last()
expected = frame_or_series([4, 3])
expected.index.name = ("a", "a")
tm.assert_equal(result, expected)
