# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
values = constant_op.constant([1, 2, 3, 4])
mask = constant_op.constant([True, True, False, True])
mt = MaskedTensorV1(values, mask)
expected = f'MaskedTensorV1(values={values!r}, mask={mask!r})'
self.assertEqual(expected, repr(mt))
