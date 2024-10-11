# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
result = pd.Series(data_for_sorting).argsort()
# argsort result gets passed to take, so should be np.intp
expected = pd.Series(np.array([2, 0, 1], dtype=np.intp))
self.assert_series_equal(result, expected)
