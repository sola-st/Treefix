# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
if callable(default):
    default = default()  # deferred construction (contains tensor)
with self.assertRaisesRegex(TypeError, error):
    extension_type_field.ExtensionTypeField(name, value_type, default)
