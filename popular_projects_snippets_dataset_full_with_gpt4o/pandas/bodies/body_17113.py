# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# fastpath - skip resort
c1 = Categorical(["a", "b"], categories=["a", "b", "c"])
c2 = Categorical(["b", "c"], categories=["a", "b", "c"])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical(["a", "b", "b", "c"], categories=["a", "b", "c"])
tm.assert_categorical_equal(result, expected)
