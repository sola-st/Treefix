# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
for dtype in [dtypes.float32, dtypes.int64, dtypes.uint32, dtypes.uint8]:
    value = np.array([[42, 43]])
    var = state_ops.variable_op(value.shape, dtype)
    self.assertShapeEqual(value, var)
    assigned = state_ops.assign(var, value)
    self.assertShapeEqual(value, assigned)
