# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
df = simple_multiindex_dataframe
arr = df.values
result = indexer(df)
expected = expected(arr)
tm.assert_series_equal(result, expected)
