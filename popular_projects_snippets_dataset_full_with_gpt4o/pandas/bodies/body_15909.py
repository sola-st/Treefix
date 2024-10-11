# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
# GH#44575
ser = Series(range(2), name="old")
ser.reset_index(name="new", drop=True, inplace=True)
expected = Series(range(2), name="old")
tm.assert_series_equal(ser, expected)
