# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
one = tensor_shape.Dimension(1)
zero = tensor_shape.Dimension(0)
has_none = tensor_shape.Dimension(None)
self.assertTrue(one)
self.assertFalse(zero)
self.assertFalse(has_none)
