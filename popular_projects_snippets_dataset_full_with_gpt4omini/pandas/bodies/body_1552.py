# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#45479 don't treat range key as positional
obj = frame_or_series(range(5), index=[3, 4, 1, 0, 2])

values = [9, 10, 11]
if obj.ndim == 2:
    values = [[9], [10], [11]]

obj.loc[range(3)] = values

expected = frame_or_series([0, 1, 10, 9, 11], index=obj.index)
tm.assert_equal(obj, expected)
