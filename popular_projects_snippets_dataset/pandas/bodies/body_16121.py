# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_sparse_accessor.py
ser = Series([1, 1, 2, 3], dtype="Sparse[int]")
return_value = ser.drop([0, 1], inplace=True)
assert return_value is None
assert ser.sparse.density == 1.0
