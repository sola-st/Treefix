# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
left = Series(["a", np.nan, "c"], dtype=dtype)
right = Series(["a", np.nan, "d"], dtype=dtype)

result = left == right
expected = Series([True, False, False])
tm.assert_series_equal(result, expected)

result = left != right
expected = Series([False, True, True])
tm.assert_series_equal(result, expected)

result = left == np.nan
expected = Series([False, False, False])
tm.assert_series_equal(result, expected)

result = left != np.nan
expected = Series([True, True, True])
tm.assert_series_equal(result, expected)
