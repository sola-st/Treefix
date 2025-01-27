# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series(data, dtype=dt)
result = s.mode(dropna)
expected = Series(expected, dtype=dt)
tm.assert_series_equal(result, expected)
