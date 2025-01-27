# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_ndarray_backed.py
shape = (3, 9)
result = DatetimeArray._empty(shape, dtype="datetime64[ns]")
assert isinstance(result, DatetimeArray)
assert result.shape == shape
