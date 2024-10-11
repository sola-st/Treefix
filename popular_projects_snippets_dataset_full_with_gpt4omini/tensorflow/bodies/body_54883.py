# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
s = tensor_shape.TensorShape(None)
# pylint: disable=g-error-prone-assert-raises
with self.assertRaisesRegex(ValueError, "Shape .+ is not fully defined"):
    s.assert_is_fully_defined()
# pylint: enable=g-error-prone-assert-raises
self.assertIsNone(s.rank)
with self.assertRaisesRegex(
    ValueError, "Cannot take the length of shape with unknown rank."):
    len(s)
self.assertFalse(s)
self.assertIsNone(s.dims)
with self.assertRaisesRegex(
    ValueError, "Cannot iterate over a shape with unknown rank."):
    for _ in tensor_shape.TensorShape(None):
        pass
