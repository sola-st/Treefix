# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt = MaskedTensorV1([1, 2, 3, 4], [True, True, False, True])
mt_spec = MaskedTensorV1.Spec.from_value(mt)
with self.assertRaisesRegex(
    AttributeError, 'Cannot mutate attribute `score` '
    'outside the custom constructor of ExtensionTypeSpec'):
    mt_spec.score = 12
with self.assertRaisesRegex(
    AttributeError, 'Cannot mutate attribute `values` '
    'outside the custom constructor of ExtensionTypeSpec'):
    mt_spec.values = constant_op.constant([4, 3, 2, 1])
with self.assertRaisesRegex(
    AttributeError, 'Cannot mutate attribute `values` '
    'outside the custom constructor of ExtensionTypeSpec'):
    del mt_spec.values
