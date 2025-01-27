# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 28401

ea_scalar, ea_dtype = ea_scalar_and_dtype

ser = Series(ea_scalar, index=range(3))
expected = Series([ea_scalar] * 3, dtype=ea_dtype)

assert ser.dtype == ea_dtype
tm.assert_series_equal(ser, expected)
