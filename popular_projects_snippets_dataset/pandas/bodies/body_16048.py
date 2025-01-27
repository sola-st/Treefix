# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
# GH31788
ser = Series(range(3), index=range(3))
df = pd.DataFrame(0.0, index=range(3), columns=range(3))

result_ser, result_df = ser.align(df, method=method)
tm.assert_series_equal(result_ser, ser)
tm.assert_frame_equal(result_df, df)
