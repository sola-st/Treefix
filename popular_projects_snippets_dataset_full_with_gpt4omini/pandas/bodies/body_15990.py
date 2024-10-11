# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# GH 17407
ser = Series(range(1, 6), index=Index(range(2, 7), name="IntIndex"))
result = ser.rename(str)
expected = ser.rename(lambda i: str(i))
tm.assert_series_equal(result, expected)

assert result.name == expected.name
