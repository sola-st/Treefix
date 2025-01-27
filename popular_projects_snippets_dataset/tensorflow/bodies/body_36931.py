# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(control_flow_ops.while_loop(
    cond, body, [constant_op.constant(0), constant_op.constant(0)]))
