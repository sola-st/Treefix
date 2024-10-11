# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#5226

# partially set with an empty object series
ser = Series(dtype=object)
ser.loc["foo"] = 1
tm.assert_series_equal(ser, Series([1], index=["foo"]))
ser.loc["bar"] = 3
tm.assert_series_equal(ser, Series([1, 3], index=["foo", "bar"]))
ser.loc[3] = 4
tm.assert_series_equal(ser, Series([1, 3, 4], index=["foo", "bar", 3]))
