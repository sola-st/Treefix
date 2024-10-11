# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
"""
        tests solely that the result is the same whether or not numexpr is
        enabled.  Need to test whether the function does the correct thing
        elsewhere.
        """
df = request.getfixturevalue(fixture)
arith = comparison_op.__name__
with option_context("compute.use_numexpr", False):
    other = df.copy() + 1

expr._MIN_ELEMENTS = 0
expr.set_test_mode(True)

result, expected = self.call_op(df, other, flex, arith)

used_numexpr = expr.get_test_result()
assert used_numexpr, "Did not use numexpr as expected."
tm.assert_equal(expected, result)
