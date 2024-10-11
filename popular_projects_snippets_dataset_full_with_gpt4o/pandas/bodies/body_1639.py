# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
mask = string_series > string_series.median()

result = string_series.copy()
result.loc[mask] = 0
expected = string_series
expected[mask] = 0
tm.assert_series_equal(result, expected)
