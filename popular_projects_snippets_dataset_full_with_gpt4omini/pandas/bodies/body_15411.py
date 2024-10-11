# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#45462
ser = Series([True, False, True])
values = ser._values
arr = array([True, False, None])

ser[:2] = arr[:2]  # no NAs -> can set inplace
assert ser._values is values

ser[1:] = arr[1:]  # has an NA -> cast to boolean dtype
expected = Series(arr)
tm.assert_series_equal(ser, expected)
