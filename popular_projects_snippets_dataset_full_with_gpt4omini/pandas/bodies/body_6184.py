# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
result = data.delete(0)
expected = data[1:]
self.assert_extension_array_equal(result, expected)

result = data.delete([1, 3])
expected = data._concat_same_type([data[[0]], data[[2]], data[4:]])
self.assert_extension_array_equal(result, expected)
