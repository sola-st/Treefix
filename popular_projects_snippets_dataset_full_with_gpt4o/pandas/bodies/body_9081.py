# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
dtype = SparseDtype("float", 0)
result = SparseDtype(dtype)
assert result.fill_value == 0
