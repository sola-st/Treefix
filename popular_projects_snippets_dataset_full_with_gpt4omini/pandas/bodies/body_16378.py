# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# going through 2D->1D path
vals = [(1,), (2,), (3,)]
ser = Series(vals)
dtype = ser.array.dtype  # PandasDtype
ser2 = Series(vals, dtype=dtype)
tm.assert_series_equal(ser, ser2)
