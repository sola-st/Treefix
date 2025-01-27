# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
result = arr.astype(arr.dtype.update_dtype(dtype))
tm.assert_sp_array_equal(result, expected)
