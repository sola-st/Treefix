# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
result = SparseDtype(str).subtype
assert result == np.dtype("object")
