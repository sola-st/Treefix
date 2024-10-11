# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#18586
series = Series([0, 1, 2], dtype="timedelta64[ns]")
series.iloc[0] = value
expected = Series([NaT, 1, 2], dtype="timedelta64[ns]")
tm.assert_series_equal(series, expected)
