# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(control_flow_ops.cond(
    constant_op.constant(True), branch_fn, lambda: 0))
