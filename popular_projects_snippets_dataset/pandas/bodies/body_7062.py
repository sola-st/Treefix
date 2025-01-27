# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py

ci = CategoricalIndex(["a", "b"], categories=["a", "b"], ordered=True)
str(ci)
tm.assert_index_equal(eval(repr(ci)), ci, exact=True)

# formatting
str(ci)

# long format
# this is not reprable
ci = CategoricalIndex(np.random.randint(0, 5, size=100))
str(ci)
