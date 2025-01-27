# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
cats = ["a", "b", "d"]
codes = np.array([0, 1, 0, 2], dtype="i8")
dtype = CategoricalDtype(["c", "b", "a"], ordered=True)
result = Categorical._from_inferred_categories(cats, codes, dtype)
expected = Categorical(
    ["a", "b", "a", "d"], categories=["c", "b", "a"], ordered=True
)
tm.assert_categorical_equal(result, expected)
