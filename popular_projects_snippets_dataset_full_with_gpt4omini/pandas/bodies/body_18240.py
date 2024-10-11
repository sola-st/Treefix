# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = holder([1, 2, 3, 4, 5], dtype=dtype, name="x")
box = Series if holder is Series else Index

result = np.sqrt(idx)
assert result.dtype == "f8" and isinstance(result, box)
exp = Index(np.sqrt(np.array([1, 2, 3, 4, 5], dtype=np.float64)), name="x")
exp = tm.box_expected(exp, box)
tm.assert_equal(result, exp)

result = np.divide(idx, 2.0)
assert result.dtype == "f8" and isinstance(result, box)
exp = Index([0.5, 1.0, 1.5, 2.0, 2.5], dtype=np.float64, name="x")
exp = tm.box_expected(exp, box)
tm.assert_equal(result, exp)

# _evaluate_numeric_binop
result = idx + 2.0
assert result.dtype == "f8" and isinstance(result, box)
exp = Index([3.0, 4.0, 5.0, 6.0, 7.0], dtype=np.float64, name="x")
exp = tm.box_expected(exp, box)
tm.assert_equal(result, exp)

result = idx - 2.0
assert result.dtype == "f8" and isinstance(result, box)
exp = Index([-1.0, 0.0, 1.0, 2.0, 3.0], dtype=np.float64, name="x")
exp = tm.box_expected(exp, box)
tm.assert_equal(result, exp)

result = idx * 1.0
assert result.dtype == "f8" and isinstance(result, box)
exp = Index([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64, name="x")
exp = tm.box_expected(exp, box)
tm.assert_equal(result, exp)

result = idx / 2.0
assert result.dtype == "f8" and isinstance(result, box)
exp = Index([0.5, 1.0, 1.5, 2.0, 2.5], dtype=np.float64, name="x")
exp = tm.box_expected(exp, box)
tm.assert_equal(result, exp)
