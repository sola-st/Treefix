# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#5226

# partially set with an empty object series
ser = Series(dtype=object)
ser.loc[1] = 1.0
tm.assert_series_equal(ser, Series([1.0], index=[1]))
ser.loc[3] = 3.0
tm.assert_series_equal(ser, Series([1.0, 3.0], index=[1, 3]))
