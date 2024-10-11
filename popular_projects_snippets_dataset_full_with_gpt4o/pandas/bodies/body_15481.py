# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# closed by GH#45121
orig = Series([0, 1, 2], index=["a", "b", "c"])

expected = Series([0, 2.7, 2], index=["a", "b", "c"])

ser = orig.copy()
ser.at["b"] = 2.7
tm.assert_series_equal(ser, expected)

ser = orig.copy()
ser.loc["b"] = 2.7
tm.assert_series_equal(ser, expected)

ser = orig.copy()
ser["b"] = 2.7
tm.assert_series_equal(ser, expected)

ser = orig.copy()
ser.iat[1] = 2.7
tm.assert_series_equal(ser, expected)

ser = orig.copy()
ser.iloc[1] = 2.7
tm.assert_series_equal(ser, expected)

orig_df = orig.to_frame("A")
expected_df = expected.to_frame("A")

df = orig_df.copy()
df.at["b", "A"] = 2.7
tm.assert_frame_equal(df, expected_df)

df = orig_df.copy()
df.loc["b", "A"] = 2.7
tm.assert_frame_equal(df, expected_df)

df = orig_df.copy()
df.iloc[1, 0] = 2.7
tm.assert_frame_equal(df, expected_df)

df = orig_df.copy()
df.iat[1, 0] = 2.7
tm.assert_frame_equal(df, expected_df)
