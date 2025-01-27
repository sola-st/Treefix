# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(["a", "b", "c"], ordered=True)
values = Categorical(["a", "b", "d"])
result = Categorical(values, dtype=dtype)
# We use dtype.categories, not values.categories
expected = Categorical(
    ["a", "b", "d"], categories=["a", "b", "c"], ordered=True
)
tm.assert_categorical_equal(result, expected)
