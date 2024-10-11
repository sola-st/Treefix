# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
if dtype.numpy_dtype == "object":
    # Different from BaseDtypeTests.test_is_not_object_type
    # because PandasDtype(object) is an object type
    assert is_object_dtype(dtype)
else:
    super().test_is_not_object_type(dtype)
