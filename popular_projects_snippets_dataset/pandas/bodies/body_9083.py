# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
a = SparseDtype(dtype, fill_value)
b = SparseDtype(dtype, fill_value)
assert a == b
assert b == a
