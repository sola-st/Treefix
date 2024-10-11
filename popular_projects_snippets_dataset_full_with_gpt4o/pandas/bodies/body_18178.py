# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#13006
result = np.float64(0) > Series([1, 2, 3])
expected = 0.0 > Series([1, 2, 3])
tm.assert_series_equal(result, expected)
result = Series([1, 2, 3]) < np.float64(0)
expected = Series([1, 2, 3]) < 0.0
tm.assert_series_equal(result, expected)
result = np.array([0, 1, 2])[0] > Series([0, 1, 2])
expected = 0.0 > Series([1, 2, 3])
tm.assert_series_equal(result, expected)
