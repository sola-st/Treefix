# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = DataFrame(
    {
        "a": ["foo", "bar", "baz"],
        "b": [3, 2, 1],
        "c": [0, 1, 2],
        "d": np.random.randn(3),
    }
)

tups = [tuple(row) for row in df[["a", "b", "c"]].values]
tups = com.asarray_tuplesafe(tups)
result = df.groupby(["a", "b", "c"], sort=True).sum()
tm.assert_numpy_array_equal(result.index.values, tups[[1, 2, 0]])

tups = [tuple(row) for row in df[["c", "a", "b"]].values]
tups = com.asarray_tuplesafe(tups)
result = df.groupby(["c", "a", "b"], sort=True).sum()
tm.assert_numpy_array_equal(result.index.values, tups)

tups = [tuple(x) for x in df[["b", "c", "a"]].values]
tups = com.asarray_tuplesafe(tups)
result = df.groupby(["b", "c", "a"], sort=True).sum()
tm.assert_numpy_array_equal(result.index.values, tups[[2, 1, 0]])

df = DataFrame(
    {"a": [0, 1, 2, 0, 1, 2], "b": [0, 0, 0, 1, 1, 1], "d": np.random.randn(6)}
)
grouped = df.groupby(["a", "b"])["d"]
result = grouped.sum()

def _check_groupby(df, result, keys, field, f=lambda x: x.sum()):
    tups = [tuple(row) for row in df[keys].values]
    tups = com.asarray_tuplesafe(tups)
    expected = f(df.groupby(tups)[field])
    for k, v in expected.items():
        assert result[k] == v

_check_groupby(df, result, ["a", "b"], "d")
