# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
df = multiindex_dataframe_random_data.T
with pytest.raises(KeyError, match=expected_error_msg):
    indexer(df)
