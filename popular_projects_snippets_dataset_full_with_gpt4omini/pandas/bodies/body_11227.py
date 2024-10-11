# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
df = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
        "E": np.random.randn(8),
    }
)

result = df.groupby("A")[["C", "D"]].mean()
result2 = df.groupby("A")[df.columns[2:4]].mean()

expected = df.loc[:, ["A", "C", "D"]].groupby("A").mean()

tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)
