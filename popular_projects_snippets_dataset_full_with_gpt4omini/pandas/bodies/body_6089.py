# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# GH#40353 this is called from getitem_block_index
result = data[..., :]
self.assert_extension_array_equal(result, data)

result = data[:, ...]
self.assert_extension_array_equal(result, data)

result = data[..., :3]
self.assert_extension_array_equal(result, data[:3])

result = data[:3, ...]
self.assert_extension_array_equal(result, data[:3])

result = data[..., ::2]
self.assert_extension_array_equal(result, data[::2])

result = data[::2, ...]
self.assert_extension_array_equal(result, data[::2])
