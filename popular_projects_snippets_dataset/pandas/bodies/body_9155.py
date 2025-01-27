# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c", "a"])

# inplace=False: the old one must not be changed
res = cat.rename_categories([1, 2, 3])
tm.assert_numpy_array_equal(
    res.__array__(), np.array([1, 2, 3, 1], dtype=np.int64)
)
tm.assert_index_equal(res.categories, Index([1, 2, 3]))

exp_cat = np.array(["a", "b", "c", "a"], dtype=np.object_)
tm.assert_numpy_array_equal(cat.__array__(), exp_cat)

exp_cat = Index(["a", "b", "c"])
tm.assert_index_equal(cat.categories, exp_cat)

# GH18862 (let rename_categories take callables)
result = cat.rename_categories(lambda x: x.upper())
expected = Categorical(["A", "B", "C", "A"])
tm.assert_categorical_equal(result, expected)
