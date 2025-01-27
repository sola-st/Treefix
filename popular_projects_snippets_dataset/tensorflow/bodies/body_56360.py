# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32, 0,
                                     (5, 5, 5))
self.assertEqual(type(spec.minimum), np.ndarray)
self.assertEqual(type(spec.maximum), np.ndarray)
self.assertAllEqual(spec.minimum, np.array(0, dtype=np.float32))
self.assertAllEqual(spec.maximum, np.array([5, 5, 5], dtype=np.float32))
