# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
c = constant_op.constant(1)
exit(control_flow_ops.while_loop(lambda i: i < 3, lambda i: i + c, [0]))
