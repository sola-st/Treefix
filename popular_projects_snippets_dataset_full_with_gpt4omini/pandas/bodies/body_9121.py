# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_sorting.py

# unordered cats are sortable
cat = Categorical(["a", "b", "b", "a"], ordered=False)
cat.sort_values()

cat = Categorical(["a", "c", "b", "d"], ordered=True)

# sort_values
res = cat.sort_values()
exp = np.array(["a", "b", "c", "d"], dtype=object)
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)

cat = Categorical(
    ["a", "c", "b", "d"], categories=["a", "b", "c", "d"], ordered=True
)
res = cat.sort_values()
exp = np.array(["a", "b", "c", "d"], dtype=object)
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)

res = cat.sort_values(ascending=False)
exp = np.array(["d", "c", "b", "a"], dtype=object)
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)

# sort (inplace order)
cat1 = cat.copy()
orig_codes = cat1._codes
cat1.sort_values(inplace=True)
assert cat1._codes is orig_codes
exp = np.array(["a", "b", "c", "d"], dtype=object)
tm.assert_numpy_array_equal(cat1.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)

# reverse
cat = Categorical(["a", "c", "c", "b", "d"], ordered=True)
res = cat.sort_values(ascending=False)
exp_val = np.array(["d", "c", "c", "b", "a"], dtype=object)
exp_categories = Index(["a", "b", "c", "d"])
tm.assert_numpy_array_equal(res.__array__(), exp_val)
tm.assert_index_equal(res.categories, exp_categories)
