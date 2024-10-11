# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ordered = string_series.sort_values()

sel = string_series[ordered > 0]
exp = string_series[string_series > 0]
tm.assert_series_equal(sel, exp)
