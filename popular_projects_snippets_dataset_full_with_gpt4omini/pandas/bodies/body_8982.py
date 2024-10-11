# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# GH #24128
sparse = SparseArray(np.array([1, 0, 0, 3, 0]), fill_value=8.0)
res = sparse.shift(1, fill_value=fill_value)
if isna(fill_value):
    fill_value = res.dtype.na_value
exp = SparseArray(np.array([fill_value, 1, 0, 0, 3]), fill_value=8.0)
tm.assert_sp_array_equal(res, exp)
