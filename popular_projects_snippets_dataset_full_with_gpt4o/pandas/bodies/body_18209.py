# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# Test Series.div as well as Series.__div__
# float/integer issue
# GH#7785
first = Series([1, 0], name="first")
second = Series([-0.01, -0.02], name="second")
expected = Series([-0.01, -np.inf])

result = second.div(first)
tm.assert_series_equal(result, expected, check_names=False)

result = second / first
tm.assert_series_equal(result, expected)
