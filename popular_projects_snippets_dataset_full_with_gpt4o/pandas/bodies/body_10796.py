# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 11558
cats = CategoricalIndex(
    ["qux", "foo", "baz", "bar"],
    categories=["foo", "bar", "baz", "qux"],
    ordered=True,
)
df = DataFrame(np.random.randn(20, 4), columns=cats)
result = df.groupby([1, 2, 3, 4] * 5).describe()

tm.assert_index_equal(result.stack().columns, cats)
tm.assert_categorical_equal(result.stack().columns.values, cats.values)
