# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
if callable(value):
    value = value()  # deferred construction (contains tensor)
if expected is None:
    expected = value
converted = extension_type_field._convert_value(
    value, value_type, ('x',),
    extension_type_field._ConversionContext.SPEC)
if isinstance(converted, (ops.Tensor, ragged_tensor.RaggedTensor)):
    self.assertAllEqual(converted, expected)
else:
    self.assertEqual(converted, expected)
