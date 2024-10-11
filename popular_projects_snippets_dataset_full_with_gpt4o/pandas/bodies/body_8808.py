# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = pd.Series([None, "a", None, "b", "c", None], dtype=dtype)
result = arr.sum(skipna=skipna)
if skipna:
    assert result == "abc"
else:
    assert pd.isna(result)
