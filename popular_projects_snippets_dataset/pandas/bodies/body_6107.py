# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.repeat(2).reshape(-1, 2)

result = arr2d.swapaxes(0, 1)
expected = arr2d.T
self.assert_extension_array_equal(result, expected)
