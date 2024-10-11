# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
if callable(value):
    value = value()  # deferred construction (contains tensor)
with self.assertRaisesRegex(TypeError, error):
    extension_type_field._convert_value(value, value_type, ('x',))
