# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
result = pd.Series(data[:5]).astype(str)
expected = pd.Series([str(x) for x in data[:5]], dtype=str)
self.assert_series_equal(result, expected)
