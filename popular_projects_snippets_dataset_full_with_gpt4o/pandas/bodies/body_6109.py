# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(-1, 1)

result = arr2d.take([0, 0, -1], axis=0)

expected = data.take([0, 0, -1]).reshape(-1, 1)
self.assert_extension_array_equal(result, expected)
