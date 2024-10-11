# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
ci = CategoricalIndex(list("aabbca"), categories=list("cab"))
tm.assert_categorical_equal(ci.values, Categorical(ci))

ci = CategoricalIndex(list("aabbca"), categories=list("cab"))
tm.assert_categorical_equal(
    ci.values, Categorical(ci.astype(object), categories=ci.categories)
)
