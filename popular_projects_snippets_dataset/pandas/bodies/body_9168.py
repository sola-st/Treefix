# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c", "a"], ordered=True)
old = cat.copy()
new = Categorical(["a", "b", np.nan, "a"], categories=["a", "b"], ordered=True)

res = cat.remove_categories("c")
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)

res = cat.remove_categories(["c"])
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)
