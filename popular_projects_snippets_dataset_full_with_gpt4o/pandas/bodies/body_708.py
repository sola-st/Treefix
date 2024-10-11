# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# starts with nan
arr = np.array([na_value, delta])
assert lib.infer_dtype(arr, skipna=True) == "timedelta"

arr = np.array([na_value, delta, na_value])
assert lib.infer_dtype(arr, skipna=True) == "timedelta"
