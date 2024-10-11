# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 17347
ser = Series(range(3), index=[1, 1, 3])
expected = Series(range(2), index=[1, 1])
result = indexer_sl(ser)[[1]]
tm.assert_series_equal(result, expected)
