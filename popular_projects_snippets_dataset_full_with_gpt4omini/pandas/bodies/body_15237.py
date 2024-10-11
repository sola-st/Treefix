# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
# https://github.com/pandas-dev/pandas/issues/34592
ser = Series([], dtype=float)
result = ser.where([])
tm.assert_series_equal(result, ser)
