# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
dim = tensor_shape.Dimension(None)
self.assertIsNone(dim.value)
self.assertEqual(dim.value, tensor_shape.Dimension(None).value)
self.assertEqual(
    tensor_shape.Dimension(None).value,
    (dim + tensor_shape.Dimension(None)).value)
self.assertEqual(
    tensor_shape.Dimension(None).value,
    (dim * tensor_shape.Dimension(None)).value)
self.assertEqual(
    tensor_shape.Dimension(None).value,
    (dim // tensor_shape.Dimension(None)).value)
self.assertEqual(
    tensor_shape.Dimension(None).value,
    dim.merge_with(tensor_shape.Dimension(None)).value)
self.assertIsNone(
    tensor_shape.Dimension(None) < tensor_shape.Dimension(None))
self.assertIsNone(
    tensor_shape.Dimension(None) <= tensor_shape.Dimension(None))
self.assertIsNone(
    tensor_shape.Dimension(None) > tensor_shape.Dimension(None))
self.assertIsNone(
    tensor_shape.Dimension(None) >= tensor_shape.Dimension(None))
