# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_update.py

ser = Series([10, 11, 12], dtype=dtype)
other = Series(other, index=[1, 3])
ser.update(other)

tm.assert_series_equal(ser, expected)
