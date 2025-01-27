# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
data = Series(np.random.randn(9))

codes = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
cats = Categorical.from_codes(codes, [0, 1, 2], ordered=True)

result = data.groupby(cats, observed=False).mean()
exp = data.groupby(codes, observed=False).mean()

exp.index = CategoricalIndex(
    exp.index, categories=cats.categories, ordered=cats.ordered
)
tm.assert_series_equal(result, exp)

codes = np.array([0, 0, 0, 1, 1, 1, 3, 3, 3])
cats = Categorical.from_codes(codes, [0, 1, 2, 3], ordered=True)

result = data.groupby(cats, observed=False).mean()
exp = data.groupby(codes, observed=False).mean().reindex(cats.categories)
exp.index = CategoricalIndex(
    exp.index, categories=cats.categories, ordered=cats.ordered
)
tm.assert_series_equal(result, exp)

cats = Categorical(
    ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
    categories=["a", "b", "c", "d"],
    ordered=True,
)
data = DataFrame({"a": [1, 1, 1, 2, 2, 2, 3, 4, 5], "b": cats})

result = data.groupby("b", observed=False).mean()
result = result["a"].values
exp = np.array([1, 2, 4, np.nan])
tm.assert_numpy_array_equal(result, exp)
