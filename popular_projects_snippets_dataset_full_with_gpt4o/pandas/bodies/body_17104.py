# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
# GH 13759
res = union_categoricals([Categorical([]), Categorical(val)])
exp = Categorical(val)
tm.assert_categorical_equal(res, exp)
