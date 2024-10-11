# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
# GH-33465
result = pd.Series(data[:5]).astype(nullable_string_dtype)
expected = pd.Series([str(x) for x in data[:5]], dtype=nullable_string_dtype)
self.assert_series_equal(result, expected)
