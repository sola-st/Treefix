# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py

# concat mixed series/frames
# G2385

# axis 1
index = date_range("01-Jan-2013", periods=10, freq="H")
arr = np.arange(10, dtype="int64")
s1 = Series(arr, index=index)
s2 = Series(arr, index=index)
df = DataFrame(arr.reshape(-1, 1), index=index)

expected = DataFrame(
    np.repeat(arr, 2).reshape(-1, 2), index=index, columns=[0, 0]
)
result = concat([df, df], axis=1)
tm.assert_frame_equal(result, expected)

expected = DataFrame(
    np.repeat(arr, 2).reshape(-1, 2), index=index, columns=[0, 1]
)
result = concat([s1, s2], axis=1)
tm.assert_frame_equal(result, expected)

expected = DataFrame(
    np.repeat(arr, 3).reshape(-1, 3), index=index, columns=[0, 1, 2]
)
result = concat([s1, s2, s1], axis=1)
tm.assert_frame_equal(result, expected)

expected = DataFrame(
    np.repeat(arr, 5).reshape(-1, 5), index=index, columns=[0, 0, 1, 2, 3]
)
result = concat([s1, df, s2, s2, s1], axis=1)
tm.assert_frame_equal(result, expected)

# with names
s1.name = "foo"
expected = DataFrame(
    np.repeat(arr, 3).reshape(-1, 3), index=index, columns=["foo", 0, 0]
)
result = concat([s1, df, s2], axis=1)
tm.assert_frame_equal(result, expected)

s2.name = "bar"
expected = DataFrame(
    np.repeat(arr, 3).reshape(-1, 3), index=index, columns=["foo", 0, "bar"]
)
result = concat([s1, df, s2], axis=1)
tm.assert_frame_equal(result, expected)

# ignore index
expected = DataFrame(
    np.repeat(arr, 3).reshape(-1, 3), index=index, columns=[0, 1, 2]
)
result = concat([s1, df, s2], axis=1, ignore_index=True)
tm.assert_frame_equal(result, expected)

# axis 0
expected = DataFrame(
    np.tile(arr, 3).reshape(-1, 1), index=index.tolist() * 3, columns=[0]
)
result = concat([s1, df, s2])
tm.assert_frame_equal(result, expected)

expected = DataFrame(np.tile(arr, 3).reshape(-1, 1), columns=[0])
result = concat([s1, df, s2], ignore_index=True)
tm.assert_frame_equal(result, expected)
