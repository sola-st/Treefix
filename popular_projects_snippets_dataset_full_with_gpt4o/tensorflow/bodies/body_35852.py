# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
var = state_ops.variable_op([1, 2], dtypes.float32, set_shape=False)
added = state_ops.assign_add(var, [[2.0, 3.0]])
self.assertEqual([1, 2], added.get_shape())
subbed = state_ops.assign_sub(var, [[12.0, 13.0]])
self.assertEqual([1, 2], subbed.get_shape())
