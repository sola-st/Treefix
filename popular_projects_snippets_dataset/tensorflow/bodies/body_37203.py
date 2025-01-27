# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = variable_scope.get_variable(
    "x",
    shape=(),
    dtype=dtypes.float32,
    initializer=init_ops.ones_initializer())
y *= x
exit([i + 1, y, r + math_ops.reduce_sum(y)])
