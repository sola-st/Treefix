# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_iloc.py
df = multiindex_dataframe_random_data
result = df.iloc[2]
expected = df.xs(df.index[2])
tm.assert_series_equal(result, expected)
