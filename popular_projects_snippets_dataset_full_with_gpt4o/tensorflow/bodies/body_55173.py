# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV2([4, 5], [True, False])
anon_x = extension_type.reinterpret(x,
                                    extension_type.AnonymousExtensionType)
self.assertAllEqual(anon_x.values, [4, 5])
self.assertAllEqual(anon_x.mask, [True, False])

round_trip_x = extension_type.reinterpret(anon_x, MaskedTensorV2)
self.assertAllEqual(round_trip_x.values, [4, 5])
self.assertAllEqual(round_trip_x.mask, [True, False])

converted_x = extension_type.reinterpret(anon_x, MaskedTensorV1)
self.assertAllEqual(converted_x.values, [4, 5])
self.assertAllEqual(converted_x.mask, [True, False])
