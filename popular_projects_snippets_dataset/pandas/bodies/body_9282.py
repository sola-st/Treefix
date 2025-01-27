# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
categories = ["b", "a", "c"]
dtype = CategoricalDtype(categories, ordered=ordered)
result = Categorical(["a", "b", "a", "c"], dtype=dtype)
expected = Categorical(
    ["a", "b", "a", "c"], categories=categories, ordered=ordered
)
tm.assert_categorical_equal(result, expected)
assert result.ordered is ordered
