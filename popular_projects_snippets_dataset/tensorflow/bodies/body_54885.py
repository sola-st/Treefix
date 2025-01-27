# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
s = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(None),
    tensor_shape.Dimension(7)
])
# pylint: disable=g-error-prone-assert-raises
with self.assertRaisesRegex(ValueError, "Shape .+ is not fully defined"):
    s.assert_is_fully_defined()
# pylint: enable=g-error-prone-assert-raises
self.assertEqual(s.rank, 3)
self.assertLen(s, 3)
self.assertTrue(s)
s.assert_has_rank(3)
self.assertEqual(tensor_shape.Dimension(3), s[0])
self.assertEqual(tensor_shape.Dimension(None).value, s.dims[1].value)
self.assertEqual(tensor_shape.Dimension(7), s.dims[2])
s.assert_same_rank([6, 3, 7])
for d1, d2 in zip(s, [3, None, 7]):
    assert tensor_shape.dimension_value(d1) == d2
