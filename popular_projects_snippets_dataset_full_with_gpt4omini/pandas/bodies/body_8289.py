# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_factorize.py
# GH#13750
idx = date_range("2016-11-06", freq="H", periods=12, tz="US/Eastern")
obj = index_or_series(idx)

arr, res = obj.factorize()
tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
tm.assert_index_equal(res, idx)
if index_or_series is Index:
    assert res.freq == idx.freq

idx = date_range("2016-06-13", freq="H", periods=12, tz="US/Eastern")
obj = index_or_series(idx)

arr, res = obj.factorize()
tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
tm.assert_index_equal(res, idx)
if index_or_series is Index:
    assert res.freq == idx.freq
