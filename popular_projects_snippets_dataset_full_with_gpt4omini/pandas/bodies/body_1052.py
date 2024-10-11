# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
s = multiindex_year_month_day_dataframe_random_data["A"]
expected = s.iloc[49]

result = indexer_sl(s)[2000, 3, 10]
assert result == expected
