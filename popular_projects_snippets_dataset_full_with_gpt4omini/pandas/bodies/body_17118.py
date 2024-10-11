# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# GH 14173
c1 = Categorical(["a", "b"])
c2 = Series(["b", "c"], dtype="category")
result = union_categoricals([c1, c2])
expected = Categorical(["a", "b", "b", "c"])
tm.assert_categorical_equal(result, expected)

c2 = CategoricalIndex(c2)
result = union_categoricals([c1, c2])
tm.assert_categorical_equal(result, expected)

c1 = Series(c1)
result = union_categoricals([c1, c2])
tm.assert_categorical_equal(result, expected)

msg = "all components to combine must be Categorical"
with pytest.raises(TypeError, match=msg):
    union_categoricals([c1, ["a", "b", "c"]])
