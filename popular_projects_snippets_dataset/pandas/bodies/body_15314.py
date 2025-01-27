# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# github.com/pandas-dev/pandas/commit/4f433773141d2eb384325714a2776bcc5b2e20f7
ser = Series(range(5), index=list(range(5)))
result = ser[list(range(5))]
tm.assert_series_equal(result, ser)
