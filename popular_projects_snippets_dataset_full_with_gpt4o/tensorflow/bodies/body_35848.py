# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
value = self._NewShapelessTensor()
shape = [1, 2]
var = state_ops.variable_op(shape, dtypes.float32)
self.assertEqual(shape, var.get_shape())
assigned = state_ops.assign(var, value, validate_shape=False)
self.assertEqual(tensor_shape.unknown_shape(), assigned.get_shape())
