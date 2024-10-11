# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_construct_object_arr.py
with pytest.raises(TypeError, match="has no len()"):
    construct_1d_object_array_from_listlike(val)
