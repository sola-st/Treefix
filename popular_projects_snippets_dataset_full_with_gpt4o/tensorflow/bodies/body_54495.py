# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
"""Tests that a user can register a CompositeTensor converter."""
x = _MyTuple((1, [2., 3.], [[4, 5], [6, 7]]))
y = ops.convert_to_tensor_or_composite(x)
self.assertFalse(tensor_util.is_tf_type(y))
self.assertIsInstance(y, _TupleTensor)
self.assertLen(y, len(x))
for x_, y_ in zip(x, y):
    self.assertIsInstance(y_, ops.Tensor)
    self.assertTrue(tensor_util.is_tf_type(y_))
    self.assertAllEqual(x_, tensor_util.constant_value(y_))
