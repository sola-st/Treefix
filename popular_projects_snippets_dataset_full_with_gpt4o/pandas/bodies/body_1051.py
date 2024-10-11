# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
s = multiindex_year_month_day_dataframe_random_data["A"]
expected = s.reindex(s.index[42:65])
expected.index = expected.index.droplevel(0).droplevel(0)

result = indexer_sl(s)[2000, 3]
tm.assert_series_equal(result, expected)
