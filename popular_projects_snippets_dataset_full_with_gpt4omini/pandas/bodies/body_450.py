# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = CategoricalDtype.construct_from_string("category")
assert is_dtype_equal(dtype, result)
msg = "Cannot construct a 'CategoricalDtype' from 'foo'"
with pytest.raises(TypeError, match=msg):
    CategoricalDtype.construct_from_string("foo")
