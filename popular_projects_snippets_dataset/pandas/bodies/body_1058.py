# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
df = multiindex_dataframe_random_data.T
expected = df.reindex(columns=df.columns[expected_slice])
expected.columns = expected.columns.droplevel(0)
result = indexer(df)
tm.assert_frame_equal(result, expected)
