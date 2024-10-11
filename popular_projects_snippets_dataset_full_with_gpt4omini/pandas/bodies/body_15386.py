# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ordered = string_series.sort_values()

copy = string_series.copy()
copy[ordered > 0] = 0

expected = string_series.copy()
expected[expected > 0] = 0

tm.assert_series_equal(copy, expected)
