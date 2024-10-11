# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
df = DataFrame(
    np.zeros((3, 2), dtype="int64"),
    columns=MultiIndex.from_tuples([("a", 0), ("a", 1)]),
)
df.at[0, "a"] = 10
expected = DataFrame(
    [[10, 10], [0, 0], [0, 0]],
    columns=MultiIndex.from_tuples([("a", 0), ("a", 1)]),
)
tm.assert_frame_equal(df, expected)
