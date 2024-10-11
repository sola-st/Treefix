# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with self.cached_session():
    value = self._NewShapelessTensor()
    var = state_ops.variable_op([1, 2], dtypes.float32, set_shape=False)
    self.assertEqual(tensor_shape.unknown_shape(), var.get_shape())
    self.assertEqual(tensor_shape.unknown_shape(),
                     state_ops.assign(var, value).get_shape())
