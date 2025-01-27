# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
# GH 28005
s = pd.Series([[1, 2], [3, 4]], index=[0, 0])
result = s.explode()
expected = pd.Series([1, 2, 3, 4], index=[0, 0, 0, 0], dtype=object)
tm.assert_series_equal(result, expected)
