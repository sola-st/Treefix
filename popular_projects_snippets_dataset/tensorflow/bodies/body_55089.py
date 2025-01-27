# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
values = constant_op.constant([1, 2, 3, 4])
mask = constant_op.constant([True, True, False, True])
mt = MaskedTensorV2(values, mask)
if context.executing_eagerly():
    expected = '<MaskedTensorV2 [1, 2, _, 4]>'
else:
    expected = f'MaskedTensorV2(values={values!r}, mask={mask!r})'

self.assertEqual(expected, repr(mt))
self.assertEqual(expected, repr(mt))
