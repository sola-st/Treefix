# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

# GH 7431
# cannot infer more than this as only a single element
arr = np.array([None], dtype="O")
result = lib.infer_dtype(arr, skipna=False)
assert result == "mixed"
result = lib.infer_dtype(arr, skipna=True)
assert result == "empty"
