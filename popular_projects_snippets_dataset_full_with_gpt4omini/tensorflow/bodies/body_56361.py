# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.BoundedTensorSpec((1, 2, 3), dtypes.float32, 0,
                                     (5, 5, 5))
with self.assertRaisesRegex(ValueError, "read-only"):
    spec.minimum[0] = -1
with self.assertRaisesRegex(ValueError, "read-only"):
    spec.maximum[0] = 100
