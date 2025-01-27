# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
ser = multiindex_year_month_day_dataframe_random_data["A"]
expected = ser.reindex(ser.index[49:51])
result = ser.loc[[(2000, 3, 10), (2000, 3, 13)]]
tm.assert_series_equal(result, expected)
