# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_arithmetic.py
op = getattr(operator, opname)
result = op(left_array, right_array)
expected = pd.array(exp, dtype="boolean")
tm.assert_extension_array_equal(result, expected)
