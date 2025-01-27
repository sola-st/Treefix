# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# dont cast these 3-like values to bool
ser = Series([True, False])
if not unique:
    ser.index = [1, 1]

indexer_sli(ser)[1] = val
assert type(ser.iloc[1]) == type(val)

expected = Series([True, val], dtype=object, index=ser.index)
if not unique and indexer_sli is not tm.iloc:
    expected = Series([val, val], dtype=object, index=[1, 1])
tm.assert_series_equal(ser, expected)
