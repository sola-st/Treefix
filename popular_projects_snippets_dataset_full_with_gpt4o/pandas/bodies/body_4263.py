# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# case that goes through numexpr and has to fall back to masked_arith_op
op = getattr(operator, opname)

arr = np.arange(_MIN_ELEMENTS + 100).reshape(_MIN_ELEMENTS // 100 + 1, -1) * 100
df = DataFrame(arr)
df["C"] = 1.0

ser = df[0]
result = getattr(df, opname)(ser, axis=0)

expected = DataFrame({col: op(df[col], ser) for col in df.columns})
tm.assert_frame_equal(result, expected)

result2 = getattr(df, opname)(ser.values, axis=0)
tm.assert_frame_equal(result2, expected)
