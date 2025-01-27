# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# new categories ordered by appearance
s = Categorical(["x", "y", "z"])
s2 = Categorical(["a", "b", "c"])
result = union_categoricals([s, s2])
expected = Categorical(
    ["x", "y", "z", "a", "b", "c"], categories=["x", "y", "z", "a", "b", "c"]
)
tm.assert_categorical_equal(result, expected)
