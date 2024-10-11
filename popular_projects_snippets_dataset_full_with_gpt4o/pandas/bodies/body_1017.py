# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py
ymd = multiindex_year_month_day_dataframe_random_data
s = ymd["A"]
result = s[5:]
expected = s.reindex(s.index[5:])
tm.assert_series_equal(result, expected)

exp = ymd["A"].copy()
s[5:] = 0
exp.values[5:] = 0
tm.assert_numpy_array_equal(s.values, exp.values)

result = ymd[5:]
expected = ymd.reindex(s.index[5:])
tm.assert_frame_equal(result, expected)
