# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
ser = Series([1, 2], dtype=dtype)
expected = Series([10, 10])
mask = np.array([False, False])

rs = ser.where(mask, [10, 10])
tm.assert_series_equal(rs, expected)

rs = ser.where(mask, 10)
tm.assert_series_equal(rs, expected)

rs = ser.where(mask, 10.0)
tm.assert_series_equal(rs, expected)

rs = ser.where(mask, [10.0, 10.0])
tm.assert_series_equal(rs, expected)

rs = ser.where(mask, [10.0, np.nan])
expected = Series([10, None], dtype="object")
tm.assert_series_equal(rs, expected)
