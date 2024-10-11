# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
cat = Categorical(["a", "b", "c"], categories=["a", "b", "c", "d"])
cat._set_categories(["a", "c", "d", "e"])
expected = Categorical(["a", "c", "d"], categories=list("acde"))
tm.assert_categorical_equal(cat, expected)

# fastpath
cat = Categorical(["a", "b", "c"], categories=["a", "b", "c", "d"])
cat._set_categories(["a", "c", "d", "e"], fastpath=True)
expected = Categorical(["a", "c", "d"], categories=list("acde"))
tm.assert_categorical_equal(cat, expected)
