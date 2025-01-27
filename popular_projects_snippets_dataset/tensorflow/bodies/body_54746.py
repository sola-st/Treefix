# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto([10, 20, 30, 40], shape=[2, 2])
self.assertTrue(tensor_util.ShapeEquals(t, [2, 2]))
self.assertTrue(tensor_util.ShapeEquals(t, (2, 2)))
self.assertTrue(
    tensor_util.ShapeEquals(t, tensor_shape.as_shape([2, 2]).as_proto()))
self.assertFalse(tensor_util.ShapeEquals(t, [5, 3]))
self.assertFalse(tensor_util.ShapeEquals(t, [1, 4]))
self.assertFalse(tensor_util.ShapeEquals(t, [4]))
