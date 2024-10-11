# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
cat = ["a", "b", "c"]
result = Categorical.from_codes([], categories=cat)
expected = Categorical([], categories=cat)

tm.assert_categorical_equal(result, expected)
