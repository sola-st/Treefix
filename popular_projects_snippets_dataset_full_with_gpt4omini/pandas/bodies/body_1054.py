# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py
s = multiindex_year_month_day_dataframe_random_data["A"]
result = s[(x > 0 for x in s)]
expected = s[s > 0]
tm.assert_series_equal(result, expected)
