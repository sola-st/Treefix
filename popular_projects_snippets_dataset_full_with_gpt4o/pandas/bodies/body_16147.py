# Extracted from ./data/repos/pandas/pandas/tests/series/test_unary.py
ser = tm.makeStringSeries()
ser.name = "series"
tm.assert_series_equal(-(ser < 0), ~(ser < 0))
