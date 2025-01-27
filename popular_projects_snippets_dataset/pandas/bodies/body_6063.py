# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
ser = pd.Series(data)
result = ser + data
expected = pd.Series(data + data)
self.assert_series_equal(result, expected)
