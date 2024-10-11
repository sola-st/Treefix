# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 15743
s = pd.Series([1, 2, 3])
result = s.replace("2", np.nan)
expected = pd.Series([1, 2, 3])
tm.assert_series_equal(expected, result)
