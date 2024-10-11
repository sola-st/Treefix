# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertEqual(
    tensor_shape.Dimension(12),
    tensor_shape.as_dimension(tensor_shape.Dimension(12)))
self.assertEqual(tensor_shape.Dimension(12), tensor_shape.as_dimension(12))
self.assertEqual(
    tensor_shape.Dimension(None).value,
    tensor_shape.as_dimension(tensor_shape.Dimension(None)).value)
self.assertEqual(
    tensor_shape.Dimension(None).value,
    tensor_shape.as_dimension(None).value)
