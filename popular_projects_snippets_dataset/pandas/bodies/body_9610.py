# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
arr = pd.array([1.0, 2.0, None], dtype=dtype)
result = arr.prod(skipna=skipna, min_count=min_count)
if skipna and min_count == 0:
    assert result == 2
else:
    assert result is pd.NA
