# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# GH#26154 : ensure True > False
ser = Series(data)
result = ser.nlargest(1)
expected = Series(expected)
tm.assert_series_equal(result, expected)
