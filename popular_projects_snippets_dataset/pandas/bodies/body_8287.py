# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_factorize.py
# GH#38120 freq should be preserved
idx3 = date_range("2000-01", periods=4, freq="M", tz="Asia/Tokyo")
exp_arr = np.array([0, 1, 2, 3], dtype=np.intp)

arr, idx = idx3.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, idx3)
assert idx.freq == idx3.freq

arr, idx = factorize(idx3)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, idx3)
assert idx.freq == idx3.freq
