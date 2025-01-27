# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unstack.py
index = MultiIndex(
    levels=[["bar", "foo"], ["one", "three", "two"]],
    codes=[[1, 1, 0, 0], [0, 1, 0, 2]],
)

s = Series(np.arange(4.0), index=index)
unstacked = s.unstack()

expected = DataFrame(
    [[2.0, np.nan, 3.0], [0.0, 1.0, np.nan]],
    index=["bar", "foo"],
    columns=["one", "three", "two"],
)

tm.assert_frame_equal(unstacked, expected)

unstacked = s.unstack(level=0)
tm.assert_frame_equal(unstacked, expected.T)

index = MultiIndex(
    levels=[["bar"], ["one", "two", "three"], [0, 1]],
    codes=[[0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1]],
)
s = Series(np.random.randn(6), index=index)
exp_index = MultiIndex(
    levels=[["one", "two", "three"], [0, 1]],
    codes=[[0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1]],
)
expected = DataFrame({"bar": s.values}, index=exp_index).sort_index(level=0)
unstacked = s.unstack(0).sort_index()
tm.assert_frame_equal(unstacked, expected)

# GH5873
idx = MultiIndex.from_arrays([[101, 102], [3.5, np.nan]])
ts = Series([1, 2], index=idx)
left = ts.unstack()
right = DataFrame(
    [[np.nan, 1], [2, np.nan]], index=[101, 102], columns=[np.nan, 3.5]
)
tm.assert_frame_equal(left, right)

idx = MultiIndex.from_arrays(
    [
        ["cat", "cat", "cat", "dog", "dog"],
        ["a", "a", "b", "a", "b"],
        [1, 2, 1, 1, np.nan],
    ]
)
ts = Series([1.0, 1.1, 1.2, 1.3, 1.4], index=idx)
right = DataFrame(
    [[1.0, 1.3], [1.1, np.nan], [np.nan, 1.4], [1.2, np.nan]],
    columns=["cat", "dog"],
)
tpls = [("a", 1), ("a", 2), ("b", np.nan), ("b", 1)]
right.index = MultiIndex.from_tuples(tpls)
tm.assert_frame_equal(ts.unstack(level=0), right)
