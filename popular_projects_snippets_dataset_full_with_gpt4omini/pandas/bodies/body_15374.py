# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#38303
ser = Series([0, 0])
ser.loc[0] = Series([42], index=[index])
expected = Series([exp_value, 0])
tm.assert_series_equal(ser, expected)
