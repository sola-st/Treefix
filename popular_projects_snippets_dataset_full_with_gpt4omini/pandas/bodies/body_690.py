# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([1, 2, 3, np.int64(4), np.int32(5)], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "integer"

arr = np.array([1, 2, 3, np.int64(4), np.int32(5), "foo"], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "mixed-integer"

arr = np.array([1, 2, 3, 4, 5], dtype="i4")
result = lib.infer_dtype(arr, skipna=True)
assert result == "integer"
