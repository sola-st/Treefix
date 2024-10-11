# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
arr = data[:4]
fill_value = data[0]
result = arr.shift(1, fill_value=fill_value)
expected = data.take([0, 0, 1, 2])
self.assert_extension_array_equal(result, expected)

result = arr.shift(-2, fill_value=fill_value)
expected = data.take([2, 3, 0, 0])
self.assert_extension_array_equal(result, expected)
