# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

self.assertTrue(MaskedTensorV1._tf_extension_type_has_field('values'))
self.assertTrue(MaskedTensorV1._tf_extension_type_has_field('mask'))
self.assertFalse(MaskedTensorV1._tf_extension_type_has_field('labels'))

mt = MaskedTensorV1([0], [True])
self.assertTrue(mt._tf_extension_type_has_field('values'))
self.assertTrue(mt._tf_extension_type_has_field('mask'))
self.assertFalse(mt._tf_extension_type_has_field('labels'))
