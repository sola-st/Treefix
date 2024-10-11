# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
arr = np.random.randn(3, 5)
index = MultiIndex(
    levels=[["a", "p", "x"], ["b", "q", "y"], ["c", "r", "z"]],
    codes=[[2, 0, 1], [2, 0, 1], [2, 0, 1]],
)
df = DataFrame(arr, index=index)
expected = DataFrame(arr[1:2], index=[["a"], ["b"]])
result = df.xs("c", level=2)
tm.assert_frame_equal(result, expected)
