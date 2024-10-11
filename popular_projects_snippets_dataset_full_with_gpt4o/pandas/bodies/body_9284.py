# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
result = Categorical(
    ["a", "b"], categories=categories, ordered=ordered, dtype="category"
)
expected = Categorical(["a", "b"], categories=categories, ordered=ordered)
tm.assert_categorical_equal(result, expected)
