# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_object_arr.py
data = [datum1, datum2]
result = construct_1d_object_array_from_listlike(data)

# Direct comparison fails: https://github.com/numpy/numpy/issues/10218
assert result.dtype == "object"
assert list(result) == data
