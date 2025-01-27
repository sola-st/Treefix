# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_ndarray_backed.py
shape = (3, 9)
result = TimedeltaArray._empty(shape, dtype="m8[ns]")
assert isinstance(result, TimedeltaArray)
assert result.shape == shape
