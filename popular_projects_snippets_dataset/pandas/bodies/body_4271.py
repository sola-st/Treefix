# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# after arithmetic refactor, add truediv here
df = simple_frame

row = df.xs("a")
col = df["two"]
f = getattr(df, op)
op = getattr(operator, op)
tm.assert_frame_equal(f(row), op(df, row))
tm.assert_frame_equal(f(col, axis=0), op(df.T, col).T)
