# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
idx = iter(string_series.index[:10])
result = string_series.loc[idx]
tm.assert_series_equal(result, string_series[:10])
