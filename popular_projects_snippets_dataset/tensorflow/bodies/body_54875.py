# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertEqual(repr(tensor_shape.Dimension(7)), "Dimension(7)")
self.assertEqual(repr(tensor_shape.Dimension(None)), "Dimension(None)")
