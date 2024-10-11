# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertTrue(tensor_shape.unknown_shape().as_proto().unknown_rank)
self.assertFalse(tensor_shape.unknown_shape(rank=3).as_proto().unknown_rank)
self.assertFalse(
    tensor_shape.TensorShape([1, 2, 3]).as_proto().unknown_rank)
self.assertFalse(
    tensor_shape.TensorShape([1, None, 3]).as_proto().unknown_rank)
