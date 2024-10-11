# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
result = pd.Series(data_missing_for_sorting).argsort()
expected = pd.Series(np.array([1, -1, 0], dtype=np.intp))
self.assert_series_equal(result, expected)
