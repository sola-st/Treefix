# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
"""Make sure fully known TensorShape objects convert to Tensors."""
shape = tensor_shape.TensorShape([1, tensor_shape.Dimension(2)])
shape_tensor = tensor_util.shape_tensor(shape)
self.assertAllEqual((1, 2), shape_tensor)
