# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH 37910

ser1 = Series([1], dtype=dtype1)
ser2 = Series([2], dtype=dtype2)
ser1 += ser2
expected = Series([3], dtype=dtype_expected)
tm.assert_series_equal(ser1, expected)

ser1 -= ser2
expected = Series([1], dtype=dtype_expected)
tm.assert_series_equal(ser1, expected)

ser1 *= ser2
expected = Series([2], dtype=dtype_mul)
tm.assert_series_equal(ser1, expected)
