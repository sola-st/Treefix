# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 25416
# handling of 2d index in construction
df = DataFrame([[1]], columns=[[1]], index=[1, 2])
expected = DataFrame(
    [1, 1],
    index=Index([1, 2], dtype="int64"),
    columns=MultiIndex(levels=[[1]], codes=[[0]]),
)
tm.assert_frame_equal(df, expected)

df = DataFrame([[1]], columns=[[1]], index=[[1, 2]])
expected = DataFrame(
    [1, 1],
    index=MultiIndex(levels=[[1, 2]], codes=[[0, 1]]),
    columns=MultiIndex(levels=[[1]], codes=[[0]]),
)
tm.assert_frame_equal(df, expected)
