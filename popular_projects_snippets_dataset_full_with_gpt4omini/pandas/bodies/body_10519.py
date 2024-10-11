# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
categories = ["a", "b", "c"]
df = DataFrame(
    {"A": pd.Categorical(["a", "a", "b"], categories=categories), "B": [1, 2, 3]}
)
result = df.groupby("A", observed=observed).B.agg(np.nansum)
expected = Series(
    [3, 3, 0],
    index=pd.CategoricalIndex(["a", "b", "c"], categories=categories, name="A"),
    name="B",
)
if observed:
    expected = expected[expected != 0]
tm.assert_series_equal(result, expected)
