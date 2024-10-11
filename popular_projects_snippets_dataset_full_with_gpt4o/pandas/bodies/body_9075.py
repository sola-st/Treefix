# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
arr = SparseArray([True, False, True], dtype=None)
assert arr.dtype == SparseDtype(np.bool_)
assert not arr.fill_value

arr = SparseArray([True, False, True], dtype=np.bool_)
assert arr.dtype == SparseDtype(np.bool_)
assert not arr.fill_value

arr = SparseArray([True, False, True], dtype=np.bool_, fill_value=True)
assert arr.dtype == SparseDtype(np.bool_, True)
assert arr.fill_value
