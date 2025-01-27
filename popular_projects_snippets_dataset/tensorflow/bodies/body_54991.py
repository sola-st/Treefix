# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes_test.py
if shape1.dims is not None and shape2.dims is not None:
    expected_np = expected.as_list()
    zeros1 = np.zeros(shape1.as_list())
    zeros2 = np.zeros(shape2.as_list())
    self.assertAllEqual(expected_np, np.broadcast(zeros1, zeros2).shape)
    self.assertAllEqual(expected_np, np.broadcast(zeros2, zeros1).shape)
    self.assertEqual(
        expected, common_shapes.broadcast_shape(shape1, shape2))
    self.assertEqual(
        expected, common_shapes.broadcast_shape(shape2, shape1))
else:
    self.assertEqual(expected, common_shapes.broadcast_shape(shape1, shape2))
    self.assertEqual(expected, common_shapes.broadcast_shape(shape2, shape1))
