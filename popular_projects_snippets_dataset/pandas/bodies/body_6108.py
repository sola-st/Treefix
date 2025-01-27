# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.repeat(3).reshape(-1, 3)

# axis = 0
result = arr2d.delete(1, axis=0)
expected = data.delete(1).repeat(3).reshape(-1, 3)
self.assert_extension_array_equal(result, expected)

# axis = 1
result = arr2d.delete(1, axis=1)
expected = data.repeat(2).reshape(-1, 2)
self.assert_extension_array_equal(result, expected)
