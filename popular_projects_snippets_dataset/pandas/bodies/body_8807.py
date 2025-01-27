# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = pd.Series(["a", "b", "c"], dtype=dtype)
result = arr.sum(skipna=skipna)
assert result == "abc"
