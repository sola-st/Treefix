# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# starts with nan
arr = np.array([na_value, time_stamp])
assert lib.infer_dtype(arr, skipna=True) == "datetime"

arr = np.array([na_value, time_stamp, na_value])
assert lib.infer_dtype(arr, skipna=True) == "datetime"
