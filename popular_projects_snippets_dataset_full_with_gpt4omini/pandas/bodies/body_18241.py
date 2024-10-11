# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
obj = holder([1, 2, 3], dtype=dtype, name="x")
box = Series if holder is Series else Index

result = np.modf(obj)
assert isinstance(result, tuple)
exp1 = Index([0.0, 0.0, 0.0], dtype=np.float64, name="x")
exp2 = Index([1.0, 2.0, 3.0], dtype=np.float64, name="x")
tm.assert_equal(result[0], tm.box_expected(exp1, box))
tm.assert_equal(result[1], tm.box_expected(exp2, box))
