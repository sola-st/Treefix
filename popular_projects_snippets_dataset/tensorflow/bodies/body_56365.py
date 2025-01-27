# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec_1_1 = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32, 0,
                                         (5, 5, 5))
spec_1_2 = tensor_spec.BoundedTensorSpec(
    (1, 2, 3), dtypes.float32, 0.00000001, (5, 5, 5.00000000000000001))
spec_2_1 = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32, 1,
                                         (5, 5, 5))
spec_2_2 = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32,
                                         (1, 1, 1), (5, 5, 5))
spec_2_3 = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32,
                                         (1, 1, 1), 5)
spec_3_1 = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32,
                                         (2, 1, 1), (5, 5, 5))

self.assertEqual(spec_1_1, spec_1_2)
self.assertEqual(spec_1_2, spec_1_1)

self.assertNotEqual(spec_1_1, spec_2_2)
self.assertNotEqual(spec_1_1, spec_2_1)
self.assertNotEqual(spec_2_2, spec_1_1)
self.assertNotEqual(spec_2_1, spec_1_1)

self.assertEqual(spec_2_1, spec_2_2)
self.assertEqual(spec_2_2, spec_2_1)
self.assertEqual(spec_2_2, spec_2_3)

self.assertNotEqual(spec_1_1, spec_3_1)
self.assertNotEqual(spec_2_1, spec_3_1)
self.assertNotEqual(spec_2_2, spec_3_1)
