# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(None, ordered=True)
values = Categorical(["a", "b", "d"])
result = Categorical(values, dtype=dtype)
# We use values.categories, not dtype.categories
expected = Categorical(
    ["a", "b", "d"], categories=["a", "b", "d"], ordered=True
)
tm.assert_categorical_equal(result, expected)
