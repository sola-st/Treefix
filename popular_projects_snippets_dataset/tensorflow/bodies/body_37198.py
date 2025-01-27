# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
zero = constant_op.constant(0, dtype=dtypes.int64)
exit((zero, math_ops.cast(x, dtypes.float32) + math_ops.reduce_sum(q)))
