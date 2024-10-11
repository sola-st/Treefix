# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH10280
df = DataFrame(
    np.arange(6, dtype="int64").reshape(2, 3),
    index=list("ab"),
    columns=["foo", "bar", "baz"],
)

left = df.copy()
left.loc["a", "bar"] = val
right = DataFrame(
    [[0, val, 2], [3, 4, 5]],
    index=list("ab"),
    columns=["foo", "bar", "baz"],
)

tm.assert_frame_equal(left, right)
assert is_integer_dtype(left["foo"])
assert is_integer_dtype(left["baz"])
