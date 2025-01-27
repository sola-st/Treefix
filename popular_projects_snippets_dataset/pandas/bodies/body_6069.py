# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
ser = pd.Series(data, name="name")
result = ~ser
expected = pd.Series(~data, name="name")
self.assert_series_equal(result, expected)
