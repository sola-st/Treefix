# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = string_series
mask = ser > ser.median()

# passing list is OK
result = ser[list(mask)]
expected = ser[mask]
tm.assert_series_equal(result, expected)
tm.assert_index_equal(result.index, ser.index[mask])
