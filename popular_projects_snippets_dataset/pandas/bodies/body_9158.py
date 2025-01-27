# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
# GH 17336
cat = Categorical(["a", "b", "c", "d"])
res = cat.rename_categories({"a": 4, "b": 3, "c": 2, "d": 1})
expected = Index([4, 3, 2, 1])
tm.assert_index_equal(res.categories, expected)

# Test for dicts of smaller length
cat = Categorical(["a", "b", "c", "d"])
res = cat.rename_categories({"a": 1, "c": 3})

expected = Index([1, "b", 3, "d"])
tm.assert_index_equal(res.categories, expected)

# Test for dicts with bigger length
cat = Categorical(["a", "b", "c", "d"])
res = cat.rename_categories({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
expected = Index([1, 2, 3, 4])
tm.assert_index_equal(res.categories, expected)

# Test for dicts with no items from old categories
cat = Categorical(["a", "b", "c", "d"])
res = cat.rename_categories({"f": 1, "g": 3})

expected = Index(["a", "b", "c", "d"])
tm.assert_index_equal(res.categories, expected)
