# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# https://github.com/pandas-dev/pandas/issues/19096
c1 = Categorical(["a", "b", "c"], categories=["a", "b", "c"])
c2 = Categorical(["a", "b", "c"], categories=["b", "a", "c"])
result = union_categoricals([c1, c2])
expected = Categorical(
    ["a", "b", "c", "a", "b", "c"], categories=["a", "b", "c"]
)
tm.assert_categorical_equal(result, expected)
