# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
arr = SparseArray([np.nan, 1, 2, np.nan])
assert arr.dtype == SparseDtype(np.float64, np.nan)
assert arr.dtype.subtype == np.float64
assert np.isnan(arr.fill_value)

arr = SparseArray([np.nan, 1, 2, np.nan], fill_value=0)
assert arr.dtype == SparseDtype(np.float64, 0)
assert arr.fill_value == 0

arr = SparseArray([0, 1, 2, 4], dtype=np.float64)
assert arr.dtype == SparseDtype(np.float64, np.nan)
assert np.isnan(arr.fill_value)

arr = SparseArray([0, 1, 2, 4], dtype=np.int64)
assert arr.dtype == SparseDtype(np.int64, 0)
assert arr.fill_value == 0

arr = SparseArray([0, 1, 2, 4], fill_value=0, dtype=np.int64)
assert arr.dtype == SparseDtype(np.int64, 0)
assert arr.fill_value == 0

arr = SparseArray([0, 1, 2, 4], dtype=None)
assert arr.dtype == SparseDtype(np.int64, 0)
assert arr.fill_value == 0

arr = SparseArray([0, 1, 2, 4], fill_value=0, dtype=None)
assert arr.dtype == SparseDtype(np.int64, 0)
assert arr.fill_value == 0
