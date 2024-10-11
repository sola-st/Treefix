# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = MultiIndex.from_tuples(tuples)
columns = MultiIndex.from_tuples(
    [("A", "cat"), ("B", "dog"), ("B", "cat"), ("A", "dog")]
)
df = DataFrame(np.random.randn(8, 4), index=index, columns=columns)

result = df.groupby(level=0).mean()
tm.assert_index_equal(result.columns, columns)

result = df.groupby(level=0, axis=1).mean()
tm.assert_index_equal(result.index, df.index)

result = df.groupby(level=0).agg(np.mean)
tm.assert_index_equal(result.columns, columns)

result = df.groupby(level=0).apply(lambda x: x.mean())
tm.assert_index_equal(result.columns, columns)

result = df.groupby(level=0, axis=1).agg(lambda x: x.mean(1))
tm.assert_index_equal(result.columns, Index(["A", "B"]))
tm.assert_index_equal(result.index, df.index)

# add a nuisance column
sorted_columns, _ = columns.sortlevel(0)
df["A", "foo"] = "bar"
with pytest.raises(TypeError, match="Could not convert"):
    df.groupby(level=0).mean()
result = df.groupby(level=0).mean(numeric_only=True)
tm.assert_index_equal(result.columns, df.columns[:-1])
