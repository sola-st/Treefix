# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#38303
ser = Series([0, 0], dtype="object")
idxr = indexer(ser)
idxr[0] = Series([42], index=[ser_index])
expected = Series([Series([42], index=[ser_index]), 0], dtype="object")
tm.assert_series_equal(ser, expected)
