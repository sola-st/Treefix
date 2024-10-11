# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
ser = pd.Series(data_for_sorting)
result = ser.sort_values(ascending=ascending, key=sort_by_key)
expected = ser.iloc[[2, 0, 1]]
if not ascending:
    # GH 35922. Expect stable sort
    if ser.nunique() == 2:
        expected = ser.iloc[[0, 1, 2]]
    else:
        expected = ser.iloc[[1, 0, 2]]

self.assert_series_equal(result, expected)
