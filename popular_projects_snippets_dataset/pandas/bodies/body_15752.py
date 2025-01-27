# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
s = pd.Series([[[1, 2, 3]], [1, 2], 1])
result = s.explode()
expected = pd.Series([[1, 2, 3], 1, 2, 1], index=[0, 1, 1, 2])
tm.assert_series_equal(result, expected)
