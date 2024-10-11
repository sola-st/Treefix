# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 46737
ser = Series([1, 1, 3], name="foo")
result = ser.mode()
expected = Series([1], name="foo")
tm.assert_series_equal(result, expected)
