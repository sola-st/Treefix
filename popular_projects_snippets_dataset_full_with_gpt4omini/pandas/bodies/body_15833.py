# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
# GH 18521
# Check rank does not mutate series
s = Series([Timestamp("2017-01-05 10:20:27.569000"), NaT])
expected = s.copy()

s.rank()
result = s
tm.assert_series_equal(result, expected)
