# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt1 = MaskedTensorV2([1, 2, 3, 4], [True, True, False, True])
self.assertLen(nest.flatten(mt1, expand_composites=True), 2)

mt2 = extension_type.pack(mt1)
self.assertLen(nest.flatten(mt2, expand_composites=True), 1)
self.assertIsInstance(mt2.values, ops.Tensor)
self.assertAllEqual(mt2.values, [1, 2, 3, 4])
self.assertIsInstance(mt2.mask, ops.Tensor)
self.assertAllEqual(mt2.mask, [True, True, False, True])

mt3 = extension_type.unpack(mt2)
self.assertLen(nest.flatten(mt3, expand_composites=True), 2)
self.assertIsInstance(mt3.values, ops.Tensor)
self.assertAllEqual(mt3.values, [1, 2, 3, 4])
self.assertIsInstance(mt3.mask, ops.Tensor)
self.assertAllEqual(mt3.mask, [True, True, False, True])

nest.assert_same_structure(mt1, mt3, expand_composites=True)
with self.assertRaisesRegex(ValueError, "don't have the same"):  # pylint: disable=g-error-prone-assert-raises
    nest.assert_same_structure(mt1, mt2, expand_composites=True)

mt4 = MaskedTensorV1([1, 2, 3, 4], [True, True, False, True])
with self.assertRaisesRegex(
    ValueError,
    'ExtensionTypes must have a __name__ field in order to be packed.'):
    extension_type.pack(mt4)
