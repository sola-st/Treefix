# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# RangeIndex is preserved in Categories
rng = Index(range(3))

cat = Categorical(rng)
tm.assert_index_equal(cat.categories, rng, exact=True)

cat = Categorical([1, 2, 0], categories=rng)
tm.assert_index_equal(cat.categories, rng, exact=True)
