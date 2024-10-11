# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# note labels are floats
dtype = float_numpy_dtype
ser = Series(["a", "b", "c"], index=Index([0, 0.5, 1], dtype=dtype))
expected = ser.copy()

ser.loc[1] = "zoo"
expected.iloc[2] = "zoo"

tm.assert_series_equal(ser, expected)
