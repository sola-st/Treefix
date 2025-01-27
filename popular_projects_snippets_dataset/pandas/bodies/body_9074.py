# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
# GH#10648
data = np.array([False, False, True, True, False, False])
arr = SparseArray(data, fill_value=False, dtype=bool)

assert arr.dtype == SparseDtype(bool)
tm.assert_numpy_array_equal(arr.sp_values, np.array([True, True]))
# Behavior change: np.asarray densifies.
# tm.assert_numpy_array_equal(arr.sp_values, np.asarray(arr))
tm.assert_numpy_array_equal(arr.sp_index.indices, np.array([2, 3], np.int32))

dense = arr.to_dense()
assert dense.dtype == bool
tm.assert_numpy_array_equal(dense, data)
