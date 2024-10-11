# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
dim = tensor_shape.Dimension(5)
ctor, args = dim.__reduce__()
self.assertEqual(ctor, tensor_shape.Dimension)
self.assertEqual(args, (5,))
reconstructed = ctor(*args)
self.assertEqual(reconstructed, dim)
