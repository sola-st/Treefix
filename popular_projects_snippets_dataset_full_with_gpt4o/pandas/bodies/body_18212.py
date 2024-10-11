# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
didx = idx * idx

result = idx * np.array(5, dtype="int64")
tm.assert_index_equal(result, idx * 5)

arr_dtype = "uint64" if idx.dtype == np.uint64 else "int64"
result = idx * np.arange(5, dtype=arr_dtype)
tm.assert_index_equal(result, didx)
