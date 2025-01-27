# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_factorize.py
idx1 = TimedeltaIndex(["1 day", "1 day", "2 day", "2 day", "3 day", "3 day"])

exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
exp_idx = TimedeltaIndex(["1 day", "2 day", "3 day"])

arr, idx = idx1.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq

arr, idx = idx1.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq
