# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
result = PeriodDtype("period[D]")
assert is_dtype_equal(dtype, result)
result = PeriodDtype.construct_from_string("period[D]")
assert is_dtype_equal(dtype, result)

with pytest.raises(TypeError, match="list"):
    PeriodDtype.construct_from_string([1, 2, 3])
