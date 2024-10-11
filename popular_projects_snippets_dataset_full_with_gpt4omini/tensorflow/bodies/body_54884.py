# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
s = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
])
s.assert_is_fully_defined()
self.assertEqual(s.rank, 3)
self.assertLen(s, 3)
self.assertTrue(s)
s.assert_has_rank(3)
self.assertEqual([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
], s.dims)
self.assertEqual(tensor_shape.Dimension(3), s[0])
self.assertEqual(tensor_shape.Dimension(4), s[1])
self.assertEqual(tensor_shape.Dimension(7), s[2])
self.assertEqual([3, 4, 7], s.as_list())
s.assert_is_compatible_with([3, 4, 7])
s.assert_same_rank([6, 3, 7])
for d1, d2 in zip(s, [3, 4, 7]):
    assert tensor_shape.dimension_value(d1) == d2
