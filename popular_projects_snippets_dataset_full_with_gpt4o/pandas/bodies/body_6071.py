# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
ser = pd.Series(data)
result = ser.iloc[:4]
expected = pd.Series(data[:4])
self.assert_series_equal(result, expected)

result = ser.iloc[[0, 1, 2, 3]]
self.assert_series_equal(result, expected)
