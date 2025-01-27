# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
a = pd.array([0, 1, None, 3, 4], dtype=dtype)
b = pd.array([1, 2, 3, None, 5], dtype=dtype)

# array / array
expected = pd.array(exp, dtype=dtype)

op = getattr(operator, opname)
result = op(a, b)
tm.assert_extension_array_equal(result, expected)

op = getattr(ops, "r" + opname)
result = op(a, b)
tm.assert_extension_array_equal(result, expected)
