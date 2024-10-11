# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
# axis=0
ymd = multiindex_year_month_day_dataframe_random_data

month_sums = ymd.groupby("month").sum()
result = month_sums.reindex(ymd.index, level=1)
expected = ymd.groupby(level="month").transform(np.sum)

tm.assert_frame_equal(result, expected)

# Series
result = month_sums["A"].reindex(ymd.index, level=1)
expected = ymd["A"].groupby(level="month").transform(np.sum)
tm.assert_series_equal(result, expected, check_names=False)

# axis=1
month_sums = ymd.T.groupby("month", axis=1).sum()
result = month_sums.reindex(columns=ymd.index, level=1)
expected = ymd.groupby(level="month").transform(np.sum).T
tm.assert_frame_equal(result, expected)
