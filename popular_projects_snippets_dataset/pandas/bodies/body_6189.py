# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
result = type(data)._from_sequence(data, dtype=data.dtype)
self.assert_extension_array_equal(result, data)

data = data[:0]
result = type(data)._from_sequence(data, dtype=data.dtype)
self.assert_extension_array_equal(result, data)
