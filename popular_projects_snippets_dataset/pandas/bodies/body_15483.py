# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# fixed by GH#45121
ser = Series([1, 2, 3])

ser[ser == 2] += 0.5
expected = Series([1, 2.5, 3])
tm.assert_series_equal(ser, expected)

ser = Series([1, 2, 3])
ser[1] += 0.5
tm.assert_series_equal(ser, expected)

ser = Series([1, 2, 3])
ser.loc[1] += 0.5
tm.assert_series_equal(ser, expected)

ser = Series([1, 2, 3])
ser.iloc[1] += 0.5
tm.assert_series_equal(ser, expected)

ser = Series([1, 2, 3])
ser.iat[1] += 0.5
tm.assert_series_equal(ser, expected)

ser = Series([1, 2, 3])
ser.at[1] += 0.5
tm.assert_series_equal(ser, expected)
