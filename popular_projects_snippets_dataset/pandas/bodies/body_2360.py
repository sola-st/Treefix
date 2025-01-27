# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# see GH#2903
arr = np.random.randn(4, 4)
index = MultiIndex(
    levels=[["a", "b"], ["bar", "foo", "hello", "world"]],
    codes=[[0, 0, 1, 1], [0, 1, 2, 3]],
    names=["lvl0", "lvl1"],
)
df = DataFrame(arr, columns=index)
result = df.xs(key, level=level, axis=1)
expected = DataFrame(exp_arr(arr), columns=exp_index)
tm.assert_frame_equal(result, expected)
