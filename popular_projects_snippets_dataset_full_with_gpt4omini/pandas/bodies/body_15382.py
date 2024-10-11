# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ser = Series([0, 1, 2, 0])
mask = ser > 0
ser2 = ser[mask].map(str)
ser[mask] = ser2

expected = Series([0, "1", "2", 0])
tm.assert_series_equal(ser, expected)
