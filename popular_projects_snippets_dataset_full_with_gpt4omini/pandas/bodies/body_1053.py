# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
s = multiindex_year_month_day_dataframe_random_data["A"]
with pytest.raises(expected_error, match=expected_error_msg):
    indexer(s)
