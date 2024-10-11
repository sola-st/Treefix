# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
ser = pd.Series(pd.date_range("2000", periods=12))
ser[0] = None

casted = ser.astype(dtype)
assert is_dtype_equal(casted.dtype, dtype)

result = casted.astype("datetime64[ns]")
tm.assert_series_equal(result, ser)
