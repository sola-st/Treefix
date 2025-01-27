# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
left = Series(np.random.randn(10))
right = Series(np.random.randn(10))
result = getattr(left, comparison_op.__name__)(right, axis=axis)
expected = comparison_op(left, right)
tm.assert_series_equal(result, expected)
