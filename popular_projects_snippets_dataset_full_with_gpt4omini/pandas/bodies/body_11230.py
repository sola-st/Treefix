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

result = df.groupby("A")["C"].mean()

as_frame = df.loc[:, ["A", "C"]].groupby("A").mean()
as_series = as_frame.iloc[:, 0]
expected = as_series

tm.assert_series_equal(result, expected)
