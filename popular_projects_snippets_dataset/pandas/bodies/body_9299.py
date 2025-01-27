# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(categories=["a", "b", "c"])
exp = Categorical(["a", "b", "c"], ordered=False)
res = Categorical.from_codes([0, 1, 2], categories=dtype.categories)
tm.assert_categorical_equal(exp, res)

res = Categorical.from_codes([0, 1, 2], dtype=dtype)
tm.assert_categorical_equal(exp, res)
