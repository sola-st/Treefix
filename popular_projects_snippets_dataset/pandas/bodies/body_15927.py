# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_update.py
# GH 33215
series.update(other)
tm.assert_series_equal(series, expected)
