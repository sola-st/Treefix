# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#13299
inc = lambda x: x + 1

ser = Series([1, 2, -1, 4])
ser[ser < 0] = inc

expected = Series([1, 2, inc, 4])
tm.assert_series_equal(ser, expected)
