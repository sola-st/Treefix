# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
cats = ["1", "2", "bad"]
codes = np.array([0, 0, 1, 2], dtype="i8")
dtype = CategoricalDtype([1, 2])
result = Categorical._from_inferred_categories(cats, codes, dtype)
expected = Categorical([1, 1, 2, np.nan])
tm.assert_categorical_equal(result, expected)
