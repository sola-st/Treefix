# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
dtype = any_int_ea_dtype
arr = pd.array([1, 2, 3, None], dtype=dtype)
result = arr.sum(skipna=skipna, min_count=min_count)
if skipna and min_count == 0:
    assert result == 6
else:
    assert result is pd.NA
