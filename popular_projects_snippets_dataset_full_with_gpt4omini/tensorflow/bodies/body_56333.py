# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
desc = tensor_spec.TensorSpec(tensor_shape.TensorShape([1]), dtypes.float32)
self.assertEqual(desc.shape, tensor_shape.TensorShape([1]))
