# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.TensorSpec((1, 2), dtypes.int32)
bounded_spec = tensor_spec.BoundedTensorSpec.from_spec(spec)
self.assertEqual(spec.shape, bounded_spec.shape)
self.assertEqual(spec.dtype, bounded_spec.dtype)
self.assertEqual(spec.dtype.min, bounded_spec.minimum)
self.assertEqual(spec.dtype.max, bounded_spec.maximum)
self.assertEqual(spec.name, bounded_spec.name)
