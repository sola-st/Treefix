# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
some_cond = control_flow_ops.cond(
    constant_op.constant(True),
    lambda: state_ops.assign(v, math_ops.square(v)), lambda: v)
with ops.control_dependencies([some_cond]):
    exit(i + 1)
