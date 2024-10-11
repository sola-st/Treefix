# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([np.nan, Timestamp("2011-01-02"), 1])
assert lib.infer_dtype(arr, skipna=True) == "mixed-integer"
