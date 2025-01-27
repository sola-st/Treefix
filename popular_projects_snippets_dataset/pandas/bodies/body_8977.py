# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
# GH#49631 match non-sparse behavior
values = np.array(["NaT", "2016-01-02", "2016-01-03"], dtype="M8[ns]")

arr = SparseArray(values)
result = arr.astype("int64")
expected = values.astype("int64")
tm.assert_numpy_array_equal(result, expected)

# we should also be able to cast to equivalent Sparse[int64]
dtype_int64 = SparseDtype("int64", np.iinfo(np.int64).min)
result2 = arr.astype(dtype_int64)
tm.assert_numpy_array_equal(result2.to_numpy(), expected)

# GH#50087 we should match the non-sparse behavior regardless of
#  if we have a fill_value other than NaT
dtype = SparseDtype("datetime64[ns]", values[1])
arr3 = SparseArray(values, dtype=dtype)
result3 = arr3.astype("int64")
tm.assert_numpy_array_equal(result3, expected)
