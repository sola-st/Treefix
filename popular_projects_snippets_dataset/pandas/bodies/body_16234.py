# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# make sure we operate on ndarray the same as Series
left = Series([True, True, True, False, True])
right = [True, False, None, True, np.nan]

expected = Series([True, False, False, False, False])
result = left & right
tm.assert_series_equal(result, expected)
result = left & np.array(right)
tm.assert_series_equal(result, expected)
result = left & Index(right)
tm.assert_series_equal(result, expected)
result = left & Series(right)
tm.assert_series_equal(result, expected)

expected = Series([True, True, True, True, True])
result = left | right
tm.assert_series_equal(result, expected)
result = left | np.array(right)
tm.assert_series_equal(result, expected)
result = left | Index(right)
tm.assert_series_equal(result, expected)
result = left | Series(right)
tm.assert_series_equal(result, expected)

expected = Series([False, True, True, True, True])
result = left ^ right
tm.assert_series_equal(result, expected)
result = left ^ np.array(right)
tm.assert_series_equal(result, expected)
result = left ^ Index(right)
tm.assert_series_equal(result, expected)
result = left ^ Series(right)
tm.assert_series_equal(result, expected)
