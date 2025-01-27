# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
s = pd.Series([range(256)]).explode()
result = s.explode()
tm.assert_series_equal(result, s)
