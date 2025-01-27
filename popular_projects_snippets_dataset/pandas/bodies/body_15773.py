# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# see GH#16818
ser = Series([10, 9, 8, 7, 7, 7, 7, 6])
result = ser.nlargest(4, keep="all")
expected = Series([10, 9, 8, 7, 7, 7, 7])
tm.assert_series_equal(result, expected)

result = ser.nsmallest(2, keep="all")
expected = Series([6, 7, 7, 7, 7], index=[7, 3, 4, 5, 6])
tm.assert_series_equal(result, expected)
