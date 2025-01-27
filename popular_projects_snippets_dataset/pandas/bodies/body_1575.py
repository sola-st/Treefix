# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#5226

# partially set with an empty object series
ser = Series(dtype=object)
ser.loc[1] = 1
tm.assert_series_equal(ser, Series([1], index=[1]))
ser.loc[3] = 3
tm.assert_series_equal(ser, Series([1, 3], index=[1, 3]))
