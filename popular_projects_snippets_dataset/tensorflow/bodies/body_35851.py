# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
for dtype in [
    dtypes.float32, dtypes.int64, dtypes.uint32, dtypes.uint8,
    dtypes.bfloat16
]:
    var = state_ops.variable_op([1, 2], dtype)
    added = state_ops.assign_add(var, [[2, 3]])
    self.assertEqual([1, 2], added.get_shape())
    subbed = state_ops.assign_sub(var, [[12, 13]])
    self.assertEqual([1, 2], subbed.get_shape())
