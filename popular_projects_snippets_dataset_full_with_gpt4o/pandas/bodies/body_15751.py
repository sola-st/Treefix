# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
s = pd.Series(dtype=object)
result = s.explode()
expected = s.copy()
tm.assert_series_equal(result, expected)
