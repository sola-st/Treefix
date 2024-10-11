# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes_test.py
if shape1.dims is not None and shape2.dims is not None:
    zeros1 = np.zeros(shape1.as_list())
    zeros2 = np.zeros(shape2.as_list())
    with self.assertRaises(ValueError):
        np.broadcast(zeros1, zeros2)
    with self.assertRaises(ValueError):
        np.broadcast(zeros2, zeros1)
self.assertFalse(common_shapes.is_broadcast_compatible(shape1, shape2))
self.assertFalse(common_shapes.is_broadcast_compatible(shape2, shape1))
with self.assertRaises(ValueError):
    common_shapes.broadcast_shape(shape1, shape2)
with self.assertRaises(ValueError):
    common_shapes.broadcast_shape(shape2, shape1)
