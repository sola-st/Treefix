# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# starts with nan
arr = np.array([na_value, Period("2011-01", freq="D")])
assert lib.infer_dtype(arr, skipna=True) == "period"

arr = np.array([na_value, Period("2011-01", freq="D"), na_value])
assert lib.infer_dtype(arr, skipna=True) == "period"
