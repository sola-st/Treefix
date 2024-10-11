# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
if flex:
    op = lambda x, y: getattr(x, opname)(y)
    op.__name__ = opname
else:
    op = getattr(operator, opname)

with option_context("compute.use_numexpr", False):
    expected = op(df, other)

expr.get_test_result()

result = op(df, other)
exit((result, expected))
