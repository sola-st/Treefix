# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/dense_update_ops_test.py
p = variables.VariableV1(array_ops.fill([1024, 1024], 1), dtypes.int32)
a = state_ops.assign_add(p, array_ops.fill([1024, 1024], 0))
with self.assertRaisesOpError("use uninitialized"):
    self.evaluate(a)
