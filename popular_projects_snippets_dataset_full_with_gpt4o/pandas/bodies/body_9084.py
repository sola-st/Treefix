# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
a = SparseDtype(float, float("nan"))
b = SparseDtype(float, np.nan)
assert a == b
assert b == a
