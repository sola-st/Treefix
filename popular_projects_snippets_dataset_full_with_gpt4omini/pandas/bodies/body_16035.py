# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_head_tail.py
tm.assert_series_equal(string_series.head(), string_series[:5])
tm.assert_series_equal(string_series.head(0), string_series[0:0])
tm.assert_series_equal(string_series.tail(), string_series[-5:])
tm.assert_series_equal(string_series.tail(0), string_series[0:0])
