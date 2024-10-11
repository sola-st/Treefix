# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
dim = tensor_shape.Dimension(12)
self.assertEqual(12, dim.value)
self.assertEqual(12, int(dim))
self.assertEqual(dim, tensor_shape.Dimension(12))
self.assertEqual(
    tensor_shape.Dimension(15), dim + tensor_shape.Dimension(3))
self.assertEqual(tensor_shape.Dimension(15), dim + 3)
self.assertEqual(tensor_shape.Dimension(15), 3 + dim)
self.assertEqual(tensor_shape.Dimension(9), dim - 3)
self.assertEqual(tensor_shape.Dimension(1), 13 - dim)
self.assertEqual(
    tensor_shape.Dimension(24), dim * tensor_shape.Dimension(2))
self.assertEqual(tensor_shape.Dimension(24), dim * 2)
self.assertEqual(tensor_shape.Dimension(24), 2 * dim)
self.assertEqual([4] * 12, [4] * dim)
self.assertEqual(12 * [4], dim * [4])
self.assertEqual(tensor_shape.Dimension(24), 2 * dim)
self.assertEqual(
    tensor_shape.Dimension(6), dim // tensor_shape.Dimension(2))
self.assertEqual(tensor_shape.Dimension(6), dim // 2)
self.assertEqual(tensor_shape.Dimension(0), 2 // dim)
self.assertEqual(
    tensor_shape.Dimension(12), dim.merge_with(tensor_shape.Dimension(12)))
self.assertEqual(tensor_shape.Dimension(12), dim.merge_with(12))
self.assertLess(tensor_shape.Dimension(12), tensor_shape.Dimension(13))
self.assertGreater(tensor_shape.Dimension(13), tensor_shape.Dimension(12))
self.assertLessEqual(tensor_shape.Dimension(12), tensor_shape.Dimension(12))
self.assertLessEqual(tensor_shape.Dimension(12), tensor_shape.Dimension(13))
self.assertGreater(tensor_shape.Dimension(13), tensor_shape.Dimension(12))
self.assertGreaterEqual(
    tensor_shape.Dimension(12), tensor_shape.Dimension(12))
self.assertGreaterEqual(
    tensor_shape.Dimension(13), tensor_shape.Dimension(12))
self.assertNotEqual(dim, (12,))
with self.assertRaises(ValueError):
    dim.merge_with(tensor_shape.Dimension(13))
