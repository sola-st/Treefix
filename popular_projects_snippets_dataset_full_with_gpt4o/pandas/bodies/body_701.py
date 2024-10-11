# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array(
    [np.datetime64("2011-01-01"), np.datetime64("2011-01-01")], dtype=object
)
assert lib.infer_dtype(arr, skipna=True) == "datetime64"
