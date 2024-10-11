# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
# GH 43267
indexer = FixedForwardWindowIndexer(window_size=window_size)
result = df.groupby("a")["b"].rolling(window=indexer, min_periods=1).mean()
tm.assert_series_equal(result, expected)
