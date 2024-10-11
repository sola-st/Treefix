# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
ser = pd.Series(data_missing_for_sorting)
result = ser.sort_values(ascending=ascending, key=sort_by_key)
if ascending:
    expected = ser.iloc[[2, 0, 1]]
else:
    expected = ser.iloc[[0, 2, 1]]
self.assert_series_equal(result, expected)
