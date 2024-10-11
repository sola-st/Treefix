# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([1.0, 2.0, 3.0, np.float64(4), np.float32(5)], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "floating"

arr = np.array([1, 2, 3, np.float64(4), np.float32(5), "foo"], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "mixed-integer"

arr = np.array([1, 2, 3, 4, 5], dtype="f4")
result = lib.infer_dtype(arr, skipna=True)
assert result == "floating"

arr = np.array([1, 2, 3, 4, 5], dtype="f8")
result = lib.infer_dtype(arr, skipna=True)
assert result == "floating"
