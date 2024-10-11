# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
dti = date_range("2016-01-01", periods=3)
ser = Series(dti)
orig = ser.copy()
mask = np.zeros(3, dtype=bool)

ser[mask] = "foo"
assert ser.dtype == dti.dtype  # no-op -> dont upcast
tm.assert_series_equal(ser, orig)

ser.mask(mask, "foo", inplace=True)
assert ser.dtype == dti.dtype  # no-op -> dont upcast
tm.assert_series_equal(ser, orig)
