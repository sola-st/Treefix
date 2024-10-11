# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = data[:5].copy()
arr[:5] = data[-5:]
self.assert_extension_array_equal(arr, data[-5:])
