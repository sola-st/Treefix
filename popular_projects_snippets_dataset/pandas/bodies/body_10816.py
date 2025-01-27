# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 24880
# GH#49223 - order of results was wrong when grouping by index levels
index, _ = MultiIndex.from_product(
    [
        CategoricalIndex(["bar", "foo"], ordered=False),
        CategoricalIndex(["one", "three", "two"], ordered=False),
    ],
    names=["A", "B"],
).sortlevel()

expected = Series(data=[2, 4, np.nan, 1, np.nan, 3], index=index, name="C")
if operation == "agg":
    expected = expected.fillna(0, downcast="infer")
grouped = df_cat.groupby(["A", "B"], observed=observed)["C"]
result = getattr(grouped, operation)(sum)
tm.assert_series_equal(result, expected)
