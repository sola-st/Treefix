# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#2746
# need to upcast
ser = Series([1, 2], index=[1, 2], dtype="int64")
ser[[True, False]] = Series([0], index=[1], dtype="int64")
expected = Series([0, 2], index=[1, 2], dtype="int64")

tm.assert_series_equal(ser, expected)
