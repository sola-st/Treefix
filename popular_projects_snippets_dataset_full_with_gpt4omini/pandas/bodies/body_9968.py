# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
s = Series(range(10))
indexer = ExpandingIndexer()
result = s.rolling(indexer).mean()
expected = s.expanding().mean()
tm.assert_series_equal(result, expected)
