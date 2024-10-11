# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
factor = Categorical(["a", "b", "b", "a", "a", "c", "c", "c"], ordered=True)
tm.assert_categorical_equal(factor, factor)
