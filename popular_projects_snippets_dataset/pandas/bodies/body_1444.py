# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH#13831
# Make sure an exception is raised when a tuple exceeds the dimension of the series,
# but not list when a list is used.
ser = Series([10])
res = indexer_li(ser)[[0, 0]]
exp = Series([10, 10], index=Index([0, 0]))
tm.assert_series_equal(res, exp)
