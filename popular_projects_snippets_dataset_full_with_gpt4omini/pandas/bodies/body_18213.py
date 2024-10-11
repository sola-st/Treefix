# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
didx = idx * idx

arr_dtype = "uint64" if idx.dtype == np.uint64 else "int64"
result = idx * Series(np.arange(5, dtype=arr_dtype))
tm.assert_series_equal(result, Series(didx))
