# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
dtype = any_int_ea_dtype
arr = pd.array([0, 1, None], dtype=dtype)
func = getattr(arr, method)
result = func(skipna=skipna)
if skipna:
    assert result == (0 if method == "min" else 1)
else:
    assert result is pd.NA
