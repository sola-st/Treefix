# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH3480, apply with mixed dtype on axis=1 breaks in 0.11
df = DataFrame(
    {
        "foo1": np.random.randn(6),
        "foo2": ["one", "two", "two", "three", "one", "two"],
    }
)
result = df.apply(lambda x: x, axis=1).dtypes
expected = df.dtypes
tm.assert_series_equal(result, expected)

# GH 3610 incorrect dtype conversion with as_index=False
df = DataFrame({"c1": [1, 2, 6, 6, 8]})
df["c2"] = df.c1 / 2.0
result1 = df.groupby("c2").mean().reset_index().c2
result2 = df.groupby("c2", as_index=False).mean().c2
tm.assert_series_equal(result1, result2)
