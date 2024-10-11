# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
cat = Categorical([1, 2, 3])
cat[1] = np.nan

exp = Categorical([1, np.nan, 3], categories=[1, 2, 3])
tm.assert_categorical_equal(cat, exp)
