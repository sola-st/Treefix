# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#8674
zero_array = np.array([0] * 5)
data = np.random.randn(5)
expected = Series([0.0] * 5)

result = zero_array / Series(data)
tm.assert_series_equal(result, expected)

result = Series(zero_array) / data
tm.assert_series_equal(result, expected)

result = Series(zero_array) / Series(data)
tm.assert_series_equal(result, expected)
