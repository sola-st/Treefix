# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py

if opname == "pow":
    # TODO: get this working
    exit()

op = getattr(operator, opname)

with warnings.catch_warnings():
    # array has 0s
    msg = "invalid value encountered in divide|true_divide"
    warnings.filterwarnings("ignore", msg, RuntimeWarning)
    result = expr.evaluate(op, left, left, use_numexpr=True)
    expected = expr.evaluate(op, left, left, use_numexpr=False)
tm.assert_numpy_array_equal(result, expected)

result = expr._can_use_numexpr(op, op_str, right, right, "evaluate")
assert not result
