# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
# groupby
df = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
result = df.groupby("A").sum()
tm.assert_metadata_equivalent(df, result)
