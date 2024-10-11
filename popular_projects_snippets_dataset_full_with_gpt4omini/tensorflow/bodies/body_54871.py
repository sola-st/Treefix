# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertEqual(tensor_shape.Dimension(12), tensor_shape.Dimension(12))
self.assertNotEqual(tensor_shape.Dimension(12), tensor_shape.Dimension(13))
self.assertIsNone(
    tensor_shape.Dimension(12) == tensor_shape.Dimension(None))
self.assertIsNone(
    tensor_shape.Dimension(None) == tensor_shape.Dimension(12))
self.assertIsNone(
    tensor_shape.Dimension(None) == tensor_shape.Dimension(None))

# None indicates ambiguous comparison, but comparison vs the wrong type
# is unambiguously False.
self.assertIsNotNone(tensor_shape.Dimension(None) == 12.99)
self.assertNotEqual(tensor_shape.Dimension(None), 12.99)

# pylint: disable=singleton-comparison, g-equals-none
self.assertIsNone(tensor_shape.Dimension(None) == None)
# pylint: enable=singleton-comparison, g-equals-none
self.assertNotEqual(tensor_shape.Dimension(12), 12.99)
