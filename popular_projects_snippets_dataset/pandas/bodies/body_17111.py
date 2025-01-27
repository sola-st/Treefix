# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# GH 13846
c1 = Categorical(["x", "y", "z"])
c2 = Categorical(["a", "b", "c"])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical(
    ["x", "y", "z", "a", "b", "c"], categories=["x", "y", "z", "a", "b", "c"]
)
tm.assert_categorical_equal(result, expected)
