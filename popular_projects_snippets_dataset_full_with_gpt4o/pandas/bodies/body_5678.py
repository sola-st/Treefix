# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
c = Categorical([1, 2])
exp = c
res = Series(c).mode()._values
tm.assert_categorical_equal(res, exp)

c = Categorical([1, "a", "a"])
exp = Categorical(["a"], categories=[1, "a"])
res = Series(c).mode()._values
tm.assert_categorical_equal(res, exp)

c = Categorical([1, 1, 2, 3, 3])
exp = Categorical([1, 3], categories=[1, 2, 3])
res = Series(c).mode()._values
tm.assert_categorical_equal(res, exp)
