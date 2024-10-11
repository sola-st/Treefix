# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# setitem with an iloc list
df = DataFrame(
    np.arange(9).reshape((3, 3)), index=["A", "B", "C"], columns=["A", "B", "C"]
)
df.iloc[[0, 1], [1, 2]]
df.iloc[[0, 1], [1, 2]] += 100

expected = DataFrame(
    np.array([0, 101, 102, 3, 104, 105, 6, 7, 8]).reshape((3, 3)),
    index=["A", "B", "C"],
    columns=["A", "B", "C"],
)
tm.assert_frame_equal(df, expected)
