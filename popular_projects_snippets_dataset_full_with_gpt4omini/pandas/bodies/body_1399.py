# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
left = DataFrame(
    np.arange(6, dtype="int64").reshape(2, 3) / 10.0,
    index=list("ab"),
    columns=["foo", "bar", "baz"],
)
left.loc["a", "bar"] = "wxyz"

right = DataFrame(
    [[0, "wxyz", 0.2], [0.3, 0.4, 0.5]],
    index=list("ab"),
    columns=["foo", "bar", "baz"],
)

tm.assert_frame_equal(left, right)
assert is_float_dtype(left["foo"])
assert is_float_dtype(left["baz"])
