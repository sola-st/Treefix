# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field_test.py
fields = [
    extension_type_field.ExtensionTypeField('x', int),
    extension_type_field.ExtensionTypeField(
        'y', typing.Tuple[typing.Union[int, bool], ...]),
    extension_type_field.ExtensionTypeField('z', ops.Tensor)
]
field_values = {'x': 1, 'y': [1, True, 3], 'z': [[1, 2], [3, 4], [5, 6]]}
extension_type_field.convert_fields(fields, field_values)
self.assertEqual(set(field_values), set(['x', 'y', 'z']))
self.assertEqual(field_values['x'], 1)
self.assertEqual(field_values['y'], (1, True, 3))
self.assertIsInstance(field_values['z'], ops.Tensor)
self.assertAllEqual(field_values['z'], [[1, 2], [3, 4], [5, 6]])
