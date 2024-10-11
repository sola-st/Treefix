# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
result = pd.Series(na_value, index=[1, 2, 3], dtype=dtype)
expected = pd.Series([na_value] * 3, index=[1, 2, 3], dtype=dtype)
self.assert_series_equal(result, expected)
