# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
# float -> float
arr = SparseArray([None, None, 0, 2])
result = arr.astype("Sparse[float32]")
expected = SparseArray([None, None, 0, 2], dtype=np.dtype("float32"))
tm.assert_sp_array_equal(result, expected)

dtype = SparseDtype("float64", fill_value=0)
result = arr.astype(dtype)
expected = SparseArray._simple_new(
    np.array([0.0, 2.0], dtype=dtype.subtype), IntIndex(4, [2, 3]), dtype
)
tm.assert_sp_array_equal(result, expected)

dtype = SparseDtype("int64", 0)
result = arr.astype(dtype)
expected = SparseArray._simple_new(
    np.array([0, 2], dtype=np.int64), IntIndex(4, [2, 3]), dtype
)
tm.assert_sp_array_equal(result, expected)

arr = SparseArray([0, np.nan, 0, 1], fill_value=0)
with pytest.raises(ValueError, match="NA"):
    arr.astype("Sparse[i8]")
