# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
# pd.array(extension_array) should be idempotent...
result = pd.array(data)
self.assert_extension_array_equal(result, data)
