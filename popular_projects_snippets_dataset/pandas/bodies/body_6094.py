# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# https://github.com/pandas-dev/pandas/issues/20640
n = len(data)
result = data.take([0, -n, n - 1, -1])
expected = data.take([0, 0, n - 1, n - 1])
self.assert_extension_array_equal(result, expected)
