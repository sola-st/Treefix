# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
columns = ["A", "B", "C", "D"]
df1 = DataFrame(
    {
        "A": np.array([1, 2, 3, 4], dtype="f8"),
        "B": np.array([1, 2, 3, 4], dtype="i8"),
        "C": np.array([1, 2, 3, 4], dtype="f8"),
        "D": np.array([1, 2, 3, 4], dtype="i8"),
    },
    columns=columns,
)

df2 = DataFrame(
    {
        "A": np.array([1, 2, 3, 4], dtype="i8"),
        "B": np.array([1, 2, 3, 4], dtype="f8"),
        "C": np.array([1, 2, 3, 4], dtype="i8"),
        "D": np.array([1, 2, 3, 4], dtype="f8"),
    },
    columns=columns,
)

appended = concat([df1, df2], ignore_index=True)
expected = DataFrame(
    np.concatenate([df1.values, df2.values], axis=0), columns=columns
)
tm.assert_frame_equal(appended, expected)

df = DataFrame(np.random.randn(1, 3), index=["a"])
df2 = DataFrame(np.random.randn(1, 4), index=["b"])
result = concat([df, df2], keys=["one", "two"], names=["first", "second"])
assert result.index.names == ("first", "second")
