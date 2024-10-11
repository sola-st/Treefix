# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
s = extension_type.AnonymousExtensionType(x=12, y={'x': 55})
with self.assertRaisesRegex(AttributeError, 'Cannot set attribute `x`'):
    s.x = 22
with self.assertRaisesRegex(AttributeError, 'Cannot delete attribute `y`'):
    del s.y
with self.assertRaisesRegex(TypeError, 'does not support item assignment'):
    s.y['x'] = 66
