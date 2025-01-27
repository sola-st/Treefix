# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
s = SparseArray([1, np.nan, np.nan, 3, np.nan])
res = s.fillna(-1)
exp = SparseArray([1, -1, -1, 3, -1], fill_value=-1, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)

s = SparseArray([1, np.nan, np.nan, 3, np.nan], fill_value=0)
res = s.fillna(-1)
exp = SparseArray([1, -1, -1, 3, -1], fill_value=0, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)

s = SparseArray([1, np.nan, 0, 3, 0])
res = s.fillna(-1)
exp = SparseArray([1, -1, 0, 3, 0], fill_value=-1, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)

s = SparseArray([1, np.nan, 0, 3, 0], fill_value=0)
res = s.fillna(-1)
exp = SparseArray([1, -1, 0, 3, 0], fill_value=0, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)

s = SparseArray([np.nan, np.nan, np.nan, np.nan])
res = s.fillna(-1)
exp = SparseArray([-1, -1, -1, -1], fill_value=-1, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)

s = SparseArray([np.nan, np.nan, np.nan, np.nan], fill_value=0)
res = s.fillna(-1)
exp = SparseArray([-1, -1, -1, -1], fill_value=0, dtype=np.float64)
tm.assert_sp_array_equal(res, exp)

# float dtype's fill_value is np.nan, replaced by -1
s = SparseArray([0.0, 0.0, 0.0, 0.0])
res = s.fillna(-1)
exp = SparseArray([0.0, 0.0, 0.0, 0.0], fill_value=-1)
tm.assert_sp_array_equal(res, exp)

# int dtype shouldn't have missing. No changes.
s = SparseArray([0, 0, 0, 0])
assert s.dtype == SparseDtype(np.int64)
assert s.fill_value == 0
res = s.fillna(-1)
tm.assert_sp_array_equal(res, s)

s = SparseArray([0, 0, 0, 0], fill_value=0)
assert s.dtype == SparseDtype(np.int64)
assert s.fill_value == 0
res = s.fillna(-1)
exp = SparseArray([0, 0, 0, 0], fill_value=0)
tm.assert_sp_array_equal(res, exp)

# fill_value can be nan if there is no missing hole.
# only fill_value will be changed
s = SparseArray([0, 0, 0, 0], fill_value=np.nan)
assert s.dtype == SparseDtype(np.int64, fill_value=np.nan)
assert np.isnan(s.fill_value)
res = s.fillna(-1)
exp = SparseArray([0, 0, 0, 0], fill_value=-1)
tm.assert_sp_array_equal(res, exp)
