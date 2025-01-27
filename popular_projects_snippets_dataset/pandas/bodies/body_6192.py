# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
result = pd.Series(index=[1, 2, 3], dtype=dtype)
expected = pd.Series([na_value] * 3, index=[1, 2, 3], dtype=dtype)
self.assert_series_equal(result, expected)

# GH 33559 - empty index
result = pd.Series(index=[], dtype=dtype)
expected = pd.Series([], index=pd.Index([], dtype="object"), dtype=dtype)
self.assert_series_equal(result, expected)
