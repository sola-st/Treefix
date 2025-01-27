# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# starts with nan
arr = np.array([na_value, np.datetime64("2011-01-02")])
assert lib.infer_dtype(arr, skipna=True) == "datetime64"

arr = np.array([na_value, np.datetime64("2011-01-02"), na_value])
assert lib.infer_dtype(arr, skipna=True) == "datetime64"
