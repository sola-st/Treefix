# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
# GH 16741
df = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

ts = df.groupby("A")["B"].agg(lambda x: x.value_counts().to_dict())
expected = Series(
    [{"two": 1, "one": 1, "three": 1}, {"two": 2, "one": 2, "three": 1}],
    index=Index(["bar", "foo"], name="A"),
    name="B",
)
tm.assert_series_equal(ts, expected)
