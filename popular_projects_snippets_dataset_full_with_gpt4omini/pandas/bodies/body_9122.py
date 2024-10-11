# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_sorting.py
# see gh-12882
cat = Categorical([5, 2, np.nan, 2, np.nan], ordered=True)
exp_categories = Index([2, 5])

exp = np.array([2.0, 2.0, 5.0, np.nan, np.nan])
res = cat.sort_values()  # default arguments
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, exp_categories)

exp = np.array([np.nan, np.nan, 2.0, 2.0, 5.0])
res = cat.sort_values(ascending=True, na_position="first")
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, exp_categories)

exp = np.array([np.nan, np.nan, 5.0, 2.0, 2.0])
res = cat.sort_values(ascending=False, na_position="first")
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, exp_categories)

exp = np.array([2.0, 2.0, 5.0, np.nan, np.nan])
res = cat.sort_values(ascending=True, na_position="last")
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, exp_categories)

exp = np.array([5.0, 2.0, 2.0, np.nan, np.nan])
res = cat.sort_values(ascending=False, na_position="last")
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, exp_categories)

cat = Categorical(["a", "c", "b", "d", np.nan], ordered=True)
res = cat.sort_values(ascending=False, na_position="last")
exp_val = np.array(["d", "c", "b", "a", np.nan], dtype=object)
exp_categories = Index(["a", "b", "c", "d"])
tm.assert_numpy_array_equal(res.__array__(), exp_val)
tm.assert_index_equal(res.categories, exp_categories)

cat = Categorical(["a", "c", "b", "d", np.nan], ordered=True)
res = cat.sort_values(ascending=False, na_position="first")
exp_val = np.array([np.nan, "d", "c", "b", "a"], dtype=object)
exp_categories = Index(["a", "b", "c", "d"])
tm.assert_numpy_array_equal(res.__array__(), exp_val)
tm.assert_index_equal(res.categories, exp_categories)
