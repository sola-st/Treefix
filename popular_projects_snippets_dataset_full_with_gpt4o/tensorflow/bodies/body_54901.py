# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
s1 = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
])
s2 = tensor_shape.TensorShape([
    tensor_shape.Dimension(3),
    tensor_shape.Dimension(4),
    tensor_shape.Dimension(7)
])
s3 = tensor_shape.TensorShape(
    [tensor_shape.Dimension(3),
     tensor_shape.Dimension(4), None])

self.assertEqual(s1, s2)
self.assertEqual(s1, s2)

# Test with an unknown shape in s3
self.assertNotEqual(s1, s3)

unk0 = tensor_shape.unknown_shape()
self.assertNotEqual(unk0, s1)
self.assertNotEqual(s1, unk0)
self.assertNotEqual(unk0, s1)
self.assertNotEqual(s1, unk0)

unk1 = tensor_shape.unknown_shape()
self.assertEqual(unk0, unk1)
self.assertEqual(unk1, unk0)
