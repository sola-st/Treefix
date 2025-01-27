# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
scalar = data[0]
result = pd.Series(scalar, index=[1, 2, 3], dtype=dtype)
expected = pd.Series([scalar] * 3, index=[1, 2, 3], dtype=dtype)
self.assert_series_equal(result, expected)

result = pd.Series(scalar, index=["foo"], dtype=dtype)
expected = pd.Series([scalar], index=["foo"], dtype=dtype)
self.assert_series_equal(result, expected)
