# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = Series(range(10), index=list(range(10)))
result = ser[-12:]
tm.assert_series_equal(result, ser)

result = ser[-7:]
tm.assert_series_equal(result, ser[3:])

result = ser[:-12]
tm.assert_series_equal(result, ser[:0])
