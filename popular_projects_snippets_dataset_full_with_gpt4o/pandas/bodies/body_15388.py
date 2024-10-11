# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH: 26468
ser = Series([5, 6, 7, 8], dtype=any_numeric_ea_dtype)
ser[ser > 6] = Series(range(4), dtype=any_numeric_ea_dtype)
expected = Series([5, 6, 2, 3], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(ser, expected)

ser = Series([5, 6, 7, 8], dtype=any_numeric_ea_dtype)
ser.loc[ser > 6] = Series(range(4), dtype=any_numeric_ea_dtype)
tm.assert_series_equal(ser, expected)

ser = Series([5, 6, 7, 8], dtype=any_numeric_ea_dtype)
loc_ser = Series(range(4), dtype=any_numeric_ea_dtype)
ser.loc[ser > 6] = loc_ser.loc[loc_ser > 1]
tm.assert_series_equal(ser, expected)
