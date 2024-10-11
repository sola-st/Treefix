# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c", "a"], ordered=True)
old = cat.copy()
new = Categorical(
    ["a", "b", "c", "a"], categories=["c", "b", "a"], ordered=True
)

res = cat.reorder_categories(["c", "b", "a"])
# cat must be the same as before
tm.assert_categorical_equal(cat, old)
# only res is changed
tm.assert_categorical_equal(res, new)
