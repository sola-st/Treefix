# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_duplicated.py
ser = Series(["a", "b", "b", "c", "a"], name="name")

result = ser.duplicated(keep=keep)
tm.assert_series_equal(result, expected)
