# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_maybe_box_native.py
boxed_obj = maybe_box_native(obj)
result_dtype = type(boxed_obj)
assert result_dtype is expected_dtype
