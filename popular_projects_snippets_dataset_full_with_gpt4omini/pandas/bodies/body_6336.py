# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
cls = dtype.construct_array_type()
result = cls._empty((4,), dtype=dtype)

assert isinstance(result, cls)
# the dtype we passed is not initialized, so will not match the
#  dtype on our result.
assert result.dtype == CategoricalDtype([])
