# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertEqual(str(tensor_shape.Dimension(7)), "7")
self.assertEqual(str(tensor_shape.Dimension(None)), "?")
