# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
value = np.array([[42.0, 43.0]])
var = state_ops.variable_op(value.shape, dtypes.float32, set_shape=False)
self.assertEqual(tensor_shape.unknown_shape(), var.get_shape())
assigned = state_ops.assign(var, value, validate_shape=False)
self.assertShapeEqual(value, assigned)
