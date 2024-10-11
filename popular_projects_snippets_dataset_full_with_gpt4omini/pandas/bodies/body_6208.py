# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
valid = data_missing[1]
result = data_missing.fillna(valid)
expected = data_missing.fillna(valid)
self.assert_extension_array_equal(result, expected)
