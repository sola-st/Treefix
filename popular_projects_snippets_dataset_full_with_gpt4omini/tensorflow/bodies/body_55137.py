# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

# Can be called on a type or an instance:
fields_1 = MaskedTensorV1._tf_extension_type_fields()
fields_2 = MaskedTensorV1([0], [True])._tf_extension_type_fields()

for fields in [fields_1, fields_2]:
    self.assertLen(fields, 2)
    self.assertEqual(fields[0].name, 'values')
    self.assertEqual(fields[0].value_type, ops.Tensor)
    self.assertEqual(fields[0].default, fields[0].NO_DEFAULT)
    self.assertEqual(fields[1].name, 'mask')
    self.assertEqual(fields[1].value_type, ops.Tensor)
    self.assertEqual(fields[1].default, fields[0].NO_DEFAULT)
