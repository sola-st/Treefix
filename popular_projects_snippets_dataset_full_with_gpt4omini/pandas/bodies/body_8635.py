# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
f12 = left + 1
f22 = right + 1

op = comparison_op

result = expr.evaluate(op, left, f12, use_numexpr=True)
expected = expr.evaluate(op, left, f12, use_numexpr=False)
tm.assert_numpy_array_equal(result, expected)

result = expr._can_use_numexpr(op, op, right, f22, "evaluate")
assert not result
