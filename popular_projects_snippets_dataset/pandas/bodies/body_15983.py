# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
ser = Series(range(5), name="foo")
renamer = Series({1: 10, 2: 20})
result = ser.rename(renamer)
expected = Series(range(5), index=[0, 10, 20, 3, 4], name="foo")
tm.assert_series_equal(result, expected)
