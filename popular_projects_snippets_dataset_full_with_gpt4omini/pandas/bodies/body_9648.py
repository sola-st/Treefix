# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_indexing.py
arr = pd.array(["a", "b", "c"], dtype=string_dtype)

result = arr.searchsorted("a", side="left")
assert is_scalar(result)
assert result == 0

result = arr.searchsorted("a", side="right")
assert is_scalar(result)
assert result == 1
