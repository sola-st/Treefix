# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH-23970
df = DataFrame(
    {"a": Series([1, 1, 2], dtype="category"), "b": [1, 2, 2], "x": [1, 2, 3]}
)

result = df.groupby(["a", "b"], as_index=as_index, observed=True)["x"].sum()

tm.assert_equal(result, expected)
