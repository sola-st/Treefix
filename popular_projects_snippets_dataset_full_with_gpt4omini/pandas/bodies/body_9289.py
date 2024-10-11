# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
values = Categorical(["a", "b", "d"])
# use categories, ordered
result = Categorical(
    values, categories=["a", "b", "c"], ordered=True, dtype="category"
)
expected = Categorical(
    ["a", "b", "d"], categories=["a", "b", "c"], ordered=True
)
tm.assert_categorical_equal(result, expected)

# No string
result = Categorical(values, categories=["a", "b", "c"], ordered=True)
tm.assert_categorical_equal(result, expected)
