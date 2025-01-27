# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# fastpath
c1 = Categorical(["a", "b"], categories=["b", "a", "c"])
c2 = Categorical(["b", "c"], categories=["b", "a", "c"])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical(["a", "b", "b", "c"], categories=["b", "a", "c"])
tm.assert_categorical_equal(result, expected)
