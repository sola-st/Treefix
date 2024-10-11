# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# GH 7551
# list-of-list is set incorrectly in mixed vs. single dtyped frames
df = DataFrame(
    {"A": np.arange(5, dtype="int64"), "B": np.arange(5, 10, dtype="int64")}
)
df.iloc[2:4] = [[10, 11], [12, 13]]
expected = DataFrame({"A": [0, 1, 10, 12, 4], "B": [5, 6, 11, 13, 9]})
tm.assert_frame_equal(df, expected)

df = DataFrame(
    {"A": ["a", "b", "c", "d", "e"], "B": np.arange(5, 10, dtype="int64")}
)
df.iloc[2:4] = [["x", 11], ["y", 13]]
expected = DataFrame({"A": ["a", "b", "x", "y", "e"], "B": [5, 6, 11, 13, 9]})
tm.assert_frame_equal(df, expected)
