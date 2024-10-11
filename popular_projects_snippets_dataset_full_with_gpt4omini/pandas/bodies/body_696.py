# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# gets cast to complex on array construction
arr = np.array([1.0, 2.0, 1 + 1j])
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "complex"

arr = np.array([1.0, 2.0, 1 + 1j], dtype="O")
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "mixed"

result = lib.infer_dtype(arr[::-1], skipna=skipna)
assert result == "mixed"

# gets cast to complex on array construction
arr = np.array([1, np.nan, 1 + 1j])
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "complex"

arr = np.array([1.0, np.nan, 1 + 1j], dtype="O")
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "mixed"

# complex with nans stays complex
arr = np.array([1 + 1j, np.nan, 3 + 3j], dtype="O")
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "complex"

# test smaller complex dtype; will pass through _try_infer_map fastpath
arr = np.array([1 + 1j, np.nan, 3 + 3j], dtype=np.complex64)
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "complex"
