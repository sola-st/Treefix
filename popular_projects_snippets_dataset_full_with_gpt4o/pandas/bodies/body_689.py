# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
result = lib.infer_dtype(np.array([], dtype="i4"), skipna=skipna)
assert result == "integer"

result = lib.infer_dtype([], skipna=skipna)
assert result == "empty"

# GH 18004
arr = np.array([np.array([], dtype=object), np.array([], dtype=object)])
result = lib.infer_dtype(arr, skipna=skipna)
assert result == "empty"
