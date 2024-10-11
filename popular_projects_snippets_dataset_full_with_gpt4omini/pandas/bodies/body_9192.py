# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# GH38140
dtype = CategoricalDtype(["a", "b", "c"], ordered=ordered)

# categories are reordered based on value when ordered=False
cat = Categorical(["a", "b", "c"], dtype=dtype)
res = cat.unique()
tm.assert_categorical_equal(res, cat)

cat = Categorical(["a", "b", "a", "a"], dtype=dtype)
res = cat.unique()
tm.assert_categorical_equal(res, Categorical(["a", "b"], dtype=dtype))

cat = Categorical(["c", "a", "b", "a", "a"], dtype=dtype)
res = cat.unique()
exp_cat = Categorical(["c", "a", "b"], dtype=dtype)
tm.assert_categorical_equal(res, exp_cat)

# nan must be removed
cat = Categorical(["b", np.nan, "b", np.nan, "a"], dtype=dtype)
res = cat.unique()
exp_cat = Categorical(["b", np.nan, "a"], dtype=dtype)
tm.assert_categorical_equal(res, exp_cat)
