# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
inds = string_series.index[[3, 4, 7]]

result = string_series.copy()
result.loc[inds] = 5

expected = string_series.copy()
expected[[3, 4, 7]] = 5
tm.assert_series_equal(result, expected)

result.iloc[5:10] = 10
expected[5:10] = 10
tm.assert_series_equal(result, expected)

# set slice with indices
d1, d2 = string_series.index[[5, 15]]
result.loc[d1:d2] = 6
expected[5:16] = 6  # because it's inclusive
tm.assert_series_equal(result, expected)

# set index value
string_series.loc[d1] = 4
string_series.loc[d2] = 6
assert string_series[d1] == 4
assert string_series[d2] == 6
