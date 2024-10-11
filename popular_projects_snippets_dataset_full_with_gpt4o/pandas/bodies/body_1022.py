# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
ymd = multiindex_year_month_day_dataframe_random_data
ymd = ymd.T
result = ymd[2000, 2]

expected = ymd.reindex(columns=ymd.columns[ymd.columns.codes[1] == 1])
expected.columns = expected.columns.droplevel(0).droplevel(0)
tm.assert_frame_equal(result, expected)
