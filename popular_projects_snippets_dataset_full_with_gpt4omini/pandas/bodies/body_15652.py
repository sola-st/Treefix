# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
s = Series([1, 3, np.nan, 12, np.nan, 25])
# slinear
expected = Series([1.0, 3.0, 7.5, 12.0, 18.5, 25.0])
result = s.interpolate(method="slinear")
tm.assert_series_equal(result, expected)

result = s.interpolate(method="slinear", downcast="infer")
tm.assert_series_equal(result, expected)
# nearest
expected = Series([1, 3, 3, 12, 12, 25])
result = s.interpolate(method="nearest")
tm.assert_series_equal(result, expected.astype("float"))

result = s.interpolate(method="nearest", downcast="infer")
tm.assert_series_equal(result, expected)
# zero
expected = Series([1, 3, 3, 12, 12, 25])
result = s.interpolate(method="zero")
tm.assert_series_equal(result, expected.astype("float"))

result = s.interpolate(method="zero", downcast="infer")
tm.assert_series_equal(result, expected)
# quadratic
# GH #15662.
expected = Series([1, 3.0, 6.823529, 12.0, 18.058824, 25.0])
result = s.interpolate(method="quadratic")
tm.assert_series_equal(result, expected)

result = s.interpolate(method="quadratic", downcast="infer")
tm.assert_series_equal(result, expected)
# cubic
expected = Series([1.0, 3.0, 6.8, 12.0, 18.2, 25.0])
result = s.interpolate(method="cubic")
tm.assert_series_equal(result, expected)
