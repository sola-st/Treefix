# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
with self.assertRaisesRegex(TypeError, error):
    extension_type_field.validate_field_value_type(tp)
