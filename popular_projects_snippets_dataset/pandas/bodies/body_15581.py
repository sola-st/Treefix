# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#44241 if we have object-dtype, 'downcast="infer"' should
#  _actually_ infer

arr = np.arange(5).astype(object)
arr[3] = np.nan

ser = Series(arr)

res = ser.fillna(3, downcast="infer")
expected = Series(np.arange(5), dtype=np.int64)
tm.assert_series_equal(res, expected)

res = ser.ffill(downcast="infer")
expected = Series([0, 1, 2, 2, 4], dtype=np.int64)
tm.assert_series_equal(res, expected)

res = ser.bfill(downcast="infer")
expected = Series([0, 1, 2, 4, 4], dtype=np.int64)
tm.assert_series_equal(res, expected)

# with a non-round float present, we will downcast to float64
ser[2] = 2.5

expected = Series([0, 1, 2.5, 3, 4], dtype=np.float64)
res = ser.fillna(3, downcast="infer")
tm.assert_series_equal(res, expected)

res = ser.ffill(downcast="infer")
expected = Series([0, 1, 2.5, 2.5, 4], dtype=np.float64)
tm.assert_series_equal(res, expected)

res = ser.bfill(downcast="infer")
expected = Series([0, 1, 2.5, 4, 4], dtype=np.float64)
tm.assert_series_equal(res, expected)
