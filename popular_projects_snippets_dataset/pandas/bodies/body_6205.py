# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
result = data_missing.dropna()
expected = data_missing[[1]]
self.assert_extension_array_equal(result, expected)
