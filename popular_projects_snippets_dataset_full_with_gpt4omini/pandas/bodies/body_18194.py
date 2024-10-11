# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#26987
dtype2 = any_real_numpy_dtype
left = Series([1, 1]).astype(dtype1)
right = Series([0, 2]).astype(dtype2)

# GH#27321 pandas convention is to set 1 // 0 to np.inf, as opposed
#  to numpy which sets to np.nan; patch `expected[0]` below
expected = left // right, left % right
expected = list(expected)
expected[0] = expected[0].astype(np.float64)
expected[0][0] = np.inf
result = divmod(left, right)

tm.assert_series_equal(result[0], expected[0])
tm.assert_series_equal(result[1], expected[1])

# rdivmod case
result = divmod(left.values, right)
tm.assert_series_equal(result[0], expected[0])
tm.assert_series_equal(result[1], expected[1])
