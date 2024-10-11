# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = Series(np.random.randn(8), index=[2, 4, 6, 8, 10, 12, 14, 16])

result = ser[:4]
expected = Series(ser.values[:4], index=[2, 4, 6, 8])
tm.assert_series_equal(result, expected)
