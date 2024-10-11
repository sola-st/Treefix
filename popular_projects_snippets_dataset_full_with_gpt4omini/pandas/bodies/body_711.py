# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array(
    [Period("2011-01", freq="M"), np.datetime64("nat")], dtype=object
)
assert lib.infer_dtype(arr, skipna=False) == "mixed"

arr = np.array(
    [np.datetime64("nat"), Period("2011-01", freq="M")], dtype=object
)
assert lib.infer_dtype(arr, skipna=False) == "mixed"
