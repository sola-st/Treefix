# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
arr_data = np.array([np.nan, np.nan, 1, 2, 3, np.nan, 4, 5, np.nan, 6])
arr = SparseArray(arr_data)

cp = SparseArray(arr, copy=True)
cp.sp_values[:3] = 0
assert not (arr.sp_values[:3] == 0).any()

not_copy = SparseArray(arr)
not_copy.sp_values[:3] = 0
assert (arr.sp_values[:3] == 0).all()
