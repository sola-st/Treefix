# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c", "a"], ordered=True)
old = cat.copy()
new = Categorical(
    ["a", "b", "c", "a"], categories=["a", "b", "c", "d"], ordered=True
)

res = cat.add_categories("d")
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)

res = cat.add_categories(["d"])
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)

# GH 9927
cat = Categorical(list("abc"), ordered=True)
expected = Categorical(list("abc"), categories=list("abcde"), ordered=True)
# test with Series, np.array, index, list
res = cat.add_categories(Series(["d", "e"]))
tm.assert_categorical_equal(res, expected)
res = cat.add_categories(np.array(["d", "e"]))
tm.assert_categorical_equal(res, expected)
res = cat.add_categories(Index(["d", "e"]))
tm.assert_categorical_equal(res, expected)
res = cat.add_categories(["d", "e"])
tm.assert_categorical_equal(res, expected)
