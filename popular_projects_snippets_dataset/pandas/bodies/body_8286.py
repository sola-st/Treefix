# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_factorize.py
idx1 = DatetimeIndex(
    ["2014-01", "2014-01", "2014-02", "2014-02", "2014-03", "2014-03"]
)

exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
exp_idx = DatetimeIndex(["2014-01", "2014-02", "2014-03"])

arr, idx = idx1.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq

arr, idx = idx1.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq

# tz must be preserved
idx1 = idx1.tz_localize("Asia/Tokyo")
exp_idx = exp_idx.tz_localize("Asia/Tokyo")

arr, idx = idx1.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq

idx2 = DatetimeIndex(
    ["2014-03", "2014-03", "2014-02", "2014-01", "2014-03", "2014-01"]
)

exp_arr = np.array([2, 2, 1, 0, 2, 0], dtype=np.intp)
exp_idx = DatetimeIndex(["2014-01", "2014-02", "2014-03"])
arr, idx = idx2.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq

exp_arr = np.array([0, 0, 1, 2, 0, 2], dtype=np.intp)
exp_idx = DatetimeIndex(["2014-03", "2014-02", "2014-01"])
arr, idx = idx2.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq
