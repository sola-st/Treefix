# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
c1 = Categorical(["b", "a"], categories=["b", "a", "c"], ordered=True)
c2 = Categorical(["a", "c"], categories=["b", "a", "c"], ordered=True)
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical(
    ["b", "a", "a", "c"], categories=["b", "a", "c"], ordered=True
)
tm.assert_categorical_equal(result, expected)
