# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
dtype_instance = type(dtype).construct_from_string(dtype.name)
assert isinstance(dtype_instance, type(dtype))
