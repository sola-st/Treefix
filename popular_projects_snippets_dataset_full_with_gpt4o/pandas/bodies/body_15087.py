# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
ser = Series(dtype=any_numpy_dtype)
result = ser.array
if is_datetime64_dtype(any_numpy_dtype):
    assert isinstance(result, DatetimeArray)
elif is_timedelta64_dtype(any_numpy_dtype):
    assert isinstance(result, TimedeltaArray)
else:
    assert isinstance(result, PandasArray)
