# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_factorize.py
idx1 = PeriodIndex(
    ["2014-01", "2014-01", "2014-02", "2014-02", "2014-03", "2014-03"], freq="M"
)

exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
exp_idx = PeriodIndex(["2014-01", "2014-02", "2014-03"], freq="M")

arr, idx = idx1.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)

arr, idx = idx1.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)

idx2 = PeriodIndex(
    ["2014-03", "2014-03", "2014-02", "2014-01", "2014-03", "2014-01"], freq="M"
)

exp_arr = np.array([2, 2, 1, 0, 2, 0], dtype=np.intp)
arr, idx = idx2.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)

exp_arr = np.array([0, 0, 1, 2, 0, 2], dtype=np.intp)
exp_idx = PeriodIndex(["2014-03", "2014-02", "2014-01"], freq="M")
arr, idx = idx2.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
