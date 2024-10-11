# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# https://github.com/pandas-dev/pandas/issues/24147
a = pd.Series(data[:3])
b = pd.Series(data[2:5], index=[2, 3, 4])
result = a.combine_first(b)
expected = pd.Series(data[:5])
self.assert_series_equal(result, expected)
