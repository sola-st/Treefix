# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
# GH#10648
data = np.array([1.0, np.nan, 3], dtype=np.float32)
arr = SparseArray(data, dtype=np.float32)

assert arr.dtype == SparseDtype(np.float32)
tm.assert_numpy_array_equal(arr.sp_values, np.array([1, 3], dtype=np.float32))
# Behavior change: np.asarray densifies.
# tm.assert_numpy_array_equal(arr.sp_values, np.asarray(arr))
tm.assert_numpy_array_equal(
    arr.sp_index.indices, np.array([0, 2], dtype=np.int32)
)

dense = arr.to_dense()
assert dense.dtype == np.float32
tm.assert_numpy_array_equal(dense, data)
