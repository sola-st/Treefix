# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([True, False, True, True, True], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "boolean"

arr = np.array([np.bool_(True), np.bool_(False)], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "boolean"

arr = np.array([True, False, True, "foo"], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "mixed"

arr = np.array([True, False, True], dtype=bool)
result = lib.infer_dtype(arr, skipna=True)
assert result == "boolean"

arr = np.array([True, np.nan, False], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "boolean"

result = lib.infer_dtype(arr, skipna=False)
assert result == "mixed"
