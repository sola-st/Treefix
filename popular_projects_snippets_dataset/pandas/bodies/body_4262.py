# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# make sure we df.floordiv(ser, axis=0) matches column-wise result
arr = np.arange(3)
ser = Series(arr)
df = DataFrame({"A": ser, "B": ser})

result = df.floordiv(ser, axis=0)

expected = DataFrame({col: df[col] // ser for col in df.columns})

tm.assert_frame_equal(result, expected)

result2 = df.floordiv(ser.values, axis=0)
tm.assert_frame_equal(result2, expected)
