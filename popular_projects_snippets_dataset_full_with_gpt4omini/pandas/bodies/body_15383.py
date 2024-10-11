# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ser = Series([0, "foo", "bar", 0])
mask = Series([False, True, True, False])
ser2 = ser[mask]
ser[mask] = ser2

expected = Series([0, "foo", "bar", 0])
tm.assert_series_equal(ser, expected)
