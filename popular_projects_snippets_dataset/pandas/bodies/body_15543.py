# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_between.py
# GH 40628
series = Series(date_range("1/1/2000", periods=10))
left, right = series[[2, 7]]

result = series.between(left, right, inclusive="both")
expected = (series >= left) & (series <= right)
tm.assert_series_equal(result, expected)

result = series.between(left, right, inclusive="left")
expected = (series >= left) & (series < right)
tm.assert_series_equal(result, expected)

result = series.between(left, right, inclusive="right")
expected = (series > left) & (series <= right)
tm.assert_series_equal(result, expected)

result = series.between(left, right, inclusive="neither")
expected = (series > left) & (series < right)
tm.assert_series_equal(result, expected)
