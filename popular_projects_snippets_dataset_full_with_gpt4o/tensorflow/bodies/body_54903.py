# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
shape = tensor_shape.TensorShape([2, 3])
ctor, args = shape.__reduce__()
self.assertEqual(ctor, tensor_shape.TensorShape)
self.assertEqual(args,
                 ([tensor_shape.Dimension(2),
                   tensor_shape.Dimension(3)],))
reconstructed = ctor(*args)
self.assertEqual(reconstructed, shape)
