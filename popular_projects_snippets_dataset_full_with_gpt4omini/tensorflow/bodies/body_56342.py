# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
bounded_spec = tensor_spec.BoundedTensorSpec((1, 2), dtypes.int32, 0, 1)
spec = tensor_spec.TensorSpec.from_spec(bounded_spec)
self.assertEqual(bounded_spec.shape, spec.shape)
self.assertEqual(bounded_spec.dtype, spec.dtype)
self.assertEqual(bounded_spec.name, spec.name)
