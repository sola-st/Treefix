# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
df = ser.to_frame()

res = ser.replace(ser[1], method="pad")
expected = pd.Series([ser[0], ser[0]] + list(ser[2:]), dtype=ser.dtype)
tm.assert_series_equal(res, expected)

res_df = df.replace(ser[1], method="pad")
tm.assert_frame_equal(res_df, expected.to_frame())

ser2 = ser.copy()
res2 = ser2.replace(ser[1], method="pad", inplace=True)
assert res2 is None
tm.assert_series_equal(ser2, expected)

res_df2 = df.replace(ser[1], method="pad", inplace=True)
assert res_df2 is None
tm.assert_frame_equal(df, expected.to_frame())
