# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
left = request.getfixturevalue(left_fix)
right = request.getfixturevalue(right_fix)

def testit():
    f12 = left + 1
    f22 = right + 1

    op = comparison_op

    result = expr.evaluate(op, left, f12, use_numexpr=True)
    expected = expr.evaluate(op, left, f12, use_numexpr=False)
    tm.assert_numpy_array_equal(result, expected)

    result = expr._can_use_numexpr(op, op, right, f22, "evaluate")
    assert not result

with option_context("compute.use_numexpr", False):
    testit()

expr.set_numexpr_threads(1)
testit()
expr.set_numexpr_threads()
testit()
