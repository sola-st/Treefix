# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
c1 = Categorical(["z", "z", "z"], categories=["x", "y", "z"])
c2 = Categorical(["x", "x", "x"], categories=["x", "y", "z"])
res = union_categoricals([c1, c2])
exp = Categorical(["z", "z", "z", "x", "x", "x"], categories=["x", "y", "z"])
tm.assert_categorical_equal(res, exp)
