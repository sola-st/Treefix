# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH 47055
s = Series([1.0, NA], dtype=Float64Dtype())
s_reindex = s.reindex(range(3))
result = s_reindex.values._data
expected = np.array([1, np.NaN, np.NaN])
tm.assert_numpy_array_equal(result, expected)
with tm.assert_produces_warning(None):
    result_log = np.log(s_reindex)
    expected_log = Series([0, np.NaN, np.NaN], dtype=Float64Dtype())
    tm.assert_series_equal(result_log, expected_log)
