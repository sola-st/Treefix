# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
# GH 34932
s = pd.Series([[1, 2], [3, 4]])
result = s.explode(ignore_index=True)
expected = pd.Series([1, 2, 3, 4], index=[0, 1, 2, 3], dtype=object)
tm.assert_series_equal(result, expected)
