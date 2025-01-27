# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 13664
arr = np.array([Period("2011-01", freq="D"), Period("2011-02", freq="D")])
assert lib.infer_dtype(arr, skipna=True) == "period"

# non-homogeneous freqs -> mixed
arr = np.array([Period("2011-01", freq="D"), Period("2011-02", freq="M")])
assert lib.infer_dtype(arr, skipna=True) == "mixed"
