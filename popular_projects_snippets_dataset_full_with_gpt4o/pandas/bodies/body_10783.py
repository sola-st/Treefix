# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 24271
df = DataFrame(
    {
        "group": ["A"] * 6 + ["B"] * 6,
        "dose": ["high", "med", "low"] * 4,
        "outcomes": np.arange(12.0),
    }
)

df.dose = Categorical(df.dose, categories=["low", "med", "high"], ordered=True)

result = df.groupby("group")["dose"].value_counts()
result = result.sort_index(level=0, sort_remaining=True)
index = ["low", "med", "high", "low", "med", "high"]
index = Categorical(index, categories=["low", "med", "high"], ordered=True)
index = [["A", "A", "A", "B", "B", "B"], CategoricalIndex(index)]
index = MultiIndex.from_arrays(index, names=["group", "dose"])
expected = Series([2] * 6, index=index, name="dose")
tm.assert_series_equal(result, expected)
