# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
orig = Series([1, 2, 3], dtype="int8")
alt = np.array([999, 1000, 1001], dtype=np.int64)

mask = np.array([True, False, True])

ser = orig.copy()
ser[mask] = Series(alt)
expected = Series([999, 2, 1001])
tm.assert_series_equal(ser, expected)

ser2 = orig.copy()
ser2.mask(mask, alt, inplace=True)
tm.assert_series_equal(ser2, expected)

ser3 = orig.copy()
res = ser3.where(~mask, Series(alt))
tm.assert_series_equal(res, expected)
