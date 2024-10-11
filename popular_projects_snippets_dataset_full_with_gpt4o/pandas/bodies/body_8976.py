# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
# GH#34456 bug caused by using .view instead of .astype in astype_nansafe
arr = SparseArray([1, 2, 3])

dtype = SparseDtype(float, 0)

result = arr.astype(dtype, copy=False)
expected = SparseArray([1.0, 2.0, 3.0], fill_value=0.0)
tm.assert_sp_array_equal(result, expected)
