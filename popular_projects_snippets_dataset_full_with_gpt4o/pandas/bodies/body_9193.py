# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# GH38140
dtype = CategoricalDtype([3, 2, 1], ordered=ordered)

c = Categorical([3, 1, 2, 2, 1], dtype=dtype)
# Categorical.unique sorts categories by appearance order
# if ordered=False
exp = Categorical([3, 1, 2], dtype=dtype)
tm.assert_categorical_equal(c.unique(), exp)

tm.assert_index_equal(Index(c).unique(), Index(exp))
tm.assert_categorical_equal(Series(c).unique(), exp)

c = Categorical([1, 1, 2, 2], dtype=dtype)
exp = Categorical([1, 2], dtype=dtype)
tm.assert_categorical_equal(c.unique(), exp)
tm.assert_index_equal(Index(c).unique(), Index(exp))
tm.assert_categorical_equal(Series(c).unique(), exp)
