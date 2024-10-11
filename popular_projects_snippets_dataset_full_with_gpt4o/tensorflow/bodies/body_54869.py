# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
known = tensor_shape.Dimension(12)
unknown = tensor_shape.Dimension(None)
self.assertEqual(
    tensor_shape.Dimension(None).value, (known + unknown).value)
self.assertEqual(
    tensor_shape.Dimension(None).value, (unknown + known).value)
self.assertEqual(
    tensor_shape.Dimension(None).value, (known * unknown).value)
self.assertEqual(
    tensor_shape.Dimension(None).value, (unknown * known).value)
self.assertEqual(
    tensor_shape.Dimension(None).value, (known // unknown).value)
self.assertEqual(
    tensor_shape.Dimension(None).value, (unknown // known).value)
self.assertEqual(tensor_shape.Dimension(12), known.merge_with(unknown))
self.assertEqual(tensor_shape.Dimension(12), unknown.merge_with(known))
self.assertIsNone(tensor_shape.Dimension(12) < tensor_shape.Dimension(None))
self.assertIsNone(
    tensor_shape.Dimension(12) <= tensor_shape.Dimension(None))
self.assertIsNone(tensor_shape.Dimension(12) > tensor_shape.Dimension(None))
self.assertIsNone(
    tensor_shape.Dimension(12) >= tensor_shape.Dimension(None))
self.assertIsNone(tensor_shape.Dimension(None) < tensor_shape.Dimension(12))
self.assertIsNone(
    tensor_shape.Dimension(None) <= tensor_shape.Dimension(12))
self.assertIsNone(tensor_shape.Dimension(None) > tensor_shape.Dimension(12))
self.assertIsNone(
    tensor_shape.Dimension(None) >= tensor_shape.Dimension(12))
