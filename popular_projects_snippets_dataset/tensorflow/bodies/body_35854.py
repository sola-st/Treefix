# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
var = state_ops.variable_op([1, 2], dtypes.float32, set_shape=False)
added = state_ops.assign_add(var, self._NewShapelessTensor())
self.assertEqual(tensor_shape.unknown_shape(), added.get_shape())
subbed = state_ops.assign_sub(var, self._NewShapelessTensor())
self.assertEqual(tensor_shape.unknown_shape(), subbed.get_shape())
