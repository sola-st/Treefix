# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
data = data[~data.isna()]

valid = data[0]
result = data.fillna(valid)
assert result is not data
self.assert_extension_array_equal(result, data)

result = data.fillna(method="backfill")
assert result is not data
self.assert_extension_array_equal(result, data)
