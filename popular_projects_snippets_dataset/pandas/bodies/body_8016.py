# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
dtype = any_int_numpy_dtype
index = NumericIndex(vals, dtype=dtype)
assert index.dtype == dtype
