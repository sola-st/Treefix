# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# GH #1013
ymd = multiindex_year_month_day_dataframe_random_data
df = ymd[:5]

result = df.loc[(2000, 1, 6), ["A", "B", "C"]]
expected = df.loc[2000, 1, 6][["A", "B", "C"]]
tm.assert_series_equal(result, expected)
