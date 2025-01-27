# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# GH 40977
ser = Series([1, 2], name="foo")
result = ser.rename(None)
expected = Series([1, 2])
tm.assert_series_equal(result, expected)
