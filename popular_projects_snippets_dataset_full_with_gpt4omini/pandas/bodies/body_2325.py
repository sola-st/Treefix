# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH#44181
df = DataFrame([pd.Interval(0, 0)])
res = df.where(df.notna())
tm.assert_frame_equal(res, df)

ser = df[0]
res = ser.where(ser.notna())
tm.assert_series_equal(res, ser)
