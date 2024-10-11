# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# GH#46589
s = Series([1, 2, 3, 3, 3, None])
result = s.nsmallest(3, keep="all")
expected = Series([1.0, 2.0, 3.0, 3.0, 3.0])
tm.assert_series_equal(result, expected)

s = Series([1, 2, None, None, None])
result = s.nsmallest(3, keep="all")
expected = Series([1, 2, None, None, None])
tm.assert_series_equal(result, expected)
