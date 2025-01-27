# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
codes = pd.array([0, 1], dtype="Int64")
categories = ["a", "b"]

result = Categorical.from_codes(codes, categories=categories)
expected = Categorical.from_codes(codes.to_numpy(int), categories=categories)

tm.assert_categorical_equal(result, expected)
