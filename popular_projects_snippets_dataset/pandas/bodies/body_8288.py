# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_factorize.py
tz = tz_naive_fixture
# GH#13750
base = date_range("2016-11-05", freq="H", periods=100, tz=tz)
idx = base.repeat(5)

exp_arr = np.arange(100, dtype=np.intp).repeat(5)

obj = index_or_series(idx)

arr, res = obj.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
expected = base._with_freq(None)
tm.assert_index_equal(res, expected)
assert res.freq == expected.freq
