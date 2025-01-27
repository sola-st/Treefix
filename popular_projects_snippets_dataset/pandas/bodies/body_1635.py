# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
inds = string_series.index[[3, 4, 7]]
tm.assert_series_equal(string_series.loc[inds], string_series.reindex(inds))
tm.assert_series_equal(string_series.iloc[5::2], string_series[5::2])

# slice with indices
d1, d2 = datetime_series.index[[5, 15]]
result = datetime_series.loc[d1:d2]
expected = datetime_series.truncate(d1, d2)
tm.assert_series_equal(result, expected)

# boolean
mask = string_series > string_series.median()
tm.assert_series_equal(string_series.loc[mask], string_series[mask])

# ask for index value
assert datetime_series.loc[d1] == datetime_series[d1]
assert datetime_series.loc[d2] == datetime_series[d2]
