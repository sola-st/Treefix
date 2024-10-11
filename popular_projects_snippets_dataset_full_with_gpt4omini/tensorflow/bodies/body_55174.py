# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if callable(value):
    value = value()
with self.assertRaisesRegex((TypeError, ValueError), error):
    extension_type.reinterpret(value, new_type)
