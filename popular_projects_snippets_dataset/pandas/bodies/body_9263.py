# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH 17248
c = Categorical([])
expected = Index([])
tm.assert_index_equal(c.categories, expected)

c = Categorical([], categories=[1, 2, 3])
expected = Index([1, 2, 3], dtype=np.int64)
tm.assert_index_equal(c.categories, expected)
