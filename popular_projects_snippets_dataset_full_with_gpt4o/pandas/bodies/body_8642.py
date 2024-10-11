# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
# GH#26736 Dataframe.floordiv(Series, axis=1) fails

df = _frame
if axis == 1:
    other = df.iloc[0, :]
else:
    other = df.iloc[:, 0]

expr._MIN_ELEMENTS = 0

op_func = getattr(df, arith)

with option_context("compute.use_numexpr", False):
    expected = op_func(other, axis=axis)

result = op_func(other, axis=axis)
tm.assert_frame_equal(expected, result)
