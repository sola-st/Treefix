# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
fields = [
    extension_type_field.ExtensionTypeField('x', int),
    extension_type_field.ExtensionTypeField('y', float)
]
with self.assertRaisesRegex(ValueError, error):
    extension_type_field.convert_fields(fields, field_values)
