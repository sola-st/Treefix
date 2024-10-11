# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# check fastpath
c1 = Categorical([1, 2, 3, 4], categories=[1, 2, 3, 4])
c2 = Categorical([3, 2, 1, np.nan], categories=[1, 2, 3, 4])
res = union_categoricals([c1, c2])
exp = Categorical([1, 2, 3, 4, 3, 2, 1, np.nan], categories=[1, 2, 3, 4])
tm.assert_categorical_equal(res, exp)
