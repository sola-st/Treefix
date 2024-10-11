# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_ndarray_backed.py
dti = date_range("2016-01-01", periods=2, tz="Asia/Tokyo")
dtype = dti.dtype

shape = (0,)
result = DatetimeArray._empty(shape, dtype=dtype)
assert result.dtype == dtype
assert isinstance(result, DatetimeArray)
assert result.shape == shape
