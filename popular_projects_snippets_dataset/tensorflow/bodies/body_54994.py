# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes_test.py
actual_dims = common_shapes.broadcast_shape(shape1, shape2).dims
reflexive_actual_dims = common_shapes.broadcast_shape(shape2, shape1).dims

if actual_dims is None:
    self.assertIsNone(reflexive_actual_dims)
elif reflexive_actual_dims is None:
    self.assertIsNone(actual_dims)
else:
    self.assertEqual(len(actual_dims), len(reflexive_actual_dims))
    for actual_dim, reflexive_actual_dim in zip(
        actual_dims, reflexive_actual_dims):
        self.assertEqual(actual_dim.value, reflexive_actual_dim.value)

expected_dims = expected.dims
if expected_dims is None:
    self.assertIsNone(actual_dims)
elif actual_dims is None:
    self.assertIsNone(expected_dims)
else:
    self.assertEqual(len(expected_dims), len(actual_dims))
    for expected_dim, actual_dim in zip(expected_dims, actual_dims):
        self.assertEqual(expected_dim.value, actual_dim.value)
