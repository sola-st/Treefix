# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
zarr = SparseArray([0, 0, 1, 2, 3, 0, 4, 5, 0, 6], fill_value=0)
res = SparseArray(zarr)
assert res.fill_value == 0
tm.assert_almost_equal(res.sp_values, zarr.sp_values)
