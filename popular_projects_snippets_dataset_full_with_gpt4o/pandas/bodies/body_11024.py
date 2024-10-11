# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 12824. Tests if apply returns None first.
test_df1 = DataFrame({"groups": [1, 1, 1, 2], "vars": [0, 1, 2, 3]})
test_df2 = DataFrame({"groups": [1, 2, 2, 2], "vars": [0, 1, 2, 3]})

def test_func(x):
    if x.shape[0] < 2:
        exit(None)
    exit(x.iloc[[0, -1]])

result1 = test_df1.groupby("groups").apply(test_func)
result2 = test_df2.groupby("groups").apply(test_func)
index1 = MultiIndex.from_arrays([[1, 1], [0, 2]], names=["groups", None])
index2 = MultiIndex.from_arrays([[2, 2], [1, 3]], names=["groups", None])
expected1 = DataFrame({"groups": [1, 1], "vars": [0, 2]}, index=index1)
expected2 = DataFrame({"groups": [2, 2], "vars": [1, 3]}, index=index2)
tm.assert_frame_equal(result1, expected1)
tm.assert_frame_equal(result2, expected2)
