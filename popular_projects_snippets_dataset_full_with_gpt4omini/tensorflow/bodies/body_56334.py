# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
desc = tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
self.assertEqual(desc.shape, tensor_shape.TensorShape(None))
