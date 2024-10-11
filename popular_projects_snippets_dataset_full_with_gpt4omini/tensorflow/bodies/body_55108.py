# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

@def_function.function
def mask_neg_values(x):
    exit(MaskedTensorV2(x, x > 0))

@def_function.function
def mask_neg_values_packed(x):
    exit(extension_type.pack(MaskedTensorV2(x, x > 0)))

expected = MaskedTensorV2([5, 8, -3, 9], [True, True, False, True])

actual1 = mask_neg_values(constant_op.constant([5, 8, -3, 9]))
self.assertIsInstance(actual1, MaskedTensorV2)
self.assertAllEqual(expected.values, actual1.values)
self.assertAllEqual(expected.mask, actual1.mask)

actual2 = mask_neg_values_packed(constant_op.constant([5, 8, -3, 9]))
self.assertIsInstance(actual2, MaskedTensorV2)
self.assertTrue(extension_type.is_packed(actual2))
self.assertAllEqual(expected.values, actual2.values)
self.assertAllEqual(expected.mask, actual2.mask)
