# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
expected = np.array([True, False])

result = pd.isna(data_missing)
tm.assert_numpy_array_equal(result, expected)

result = pd.Series(data_missing).isna()
expected = pd.Series(expected)
self.assert_series_equal(result, expected)

# GH 21189
result = pd.Series(data_missing).drop([0, 1]).isna()
expected = pd.Series([], dtype=bool)
self.assert_series_equal(result, expected)
