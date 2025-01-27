# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
if callable(default):
    default = default()  # deferred construction (contains tensor)
field = extension_type_field.ExtensionTypeField(name, value_type, default)
if converted_default is not None:
    default = converted_default
self.assertEqual(field.name, name)
self.assertEqual(field.value_type, value_type)
if isinstance(default, (ops.Tensor, ragged_tensor.RaggedTensor)):
    self.assertAllEqual(field.default, default)
else:
    self.assertEqual(field.default, default)
