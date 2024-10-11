# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
sarr = SparseArray(data_missing)
expected_dtype = SparseDtype(bool, pd.isna(data_missing.dtype.fill_value))
expected = SparseArray([True, False], dtype=expected_dtype)
result = sarr.isna()
tm.assert_sp_array_equal(result, expected)

# test isna for arr without na
sarr = sarr.fillna(0)
expected_dtype = SparseDtype(bool, pd.isna(data_missing.dtype.fill_value))
expected = SparseArray([False, False], fill_value=False, dtype=expected_dtype)
self.assert_equal(sarr.isna(), expected)
