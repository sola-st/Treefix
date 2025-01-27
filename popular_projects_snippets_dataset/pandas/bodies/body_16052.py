# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
# GH#45224
left = Series(
    [2], index=pd.MultiIndex.from_tuples([(1, 4, 3)], names=["a", "d", "c"])
)
right = Series(
    [1], index=pd.MultiIndex.from_tuples([(1, 2, 3)], names=["a", "b", "c"])
)
result_left, result_right = left.align(right)

expected_left = Series(
    [2], index=pd.MultiIndex.from_tuples([(1, 3, 4, 2)], names=["a", "c", "d", "b"])
)
expected_right = Series(
    [1], index=pd.MultiIndex.from_tuples([(1, 3, 4, 2)], names=["a", "c", "d", "b"])
)
tm.assert_series_equal(result_left, expected_left)
tm.assert_series_equal(result_right, expected_right)
