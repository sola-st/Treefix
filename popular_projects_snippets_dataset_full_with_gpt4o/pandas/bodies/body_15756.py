# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
result = s.explode()
tm.assert_series_equal(result, s)
