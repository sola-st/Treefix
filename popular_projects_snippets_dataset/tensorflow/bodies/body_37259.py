# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a tensor in a nested while is OK.
def body(_):
    c = constant_op.constant(1)
    exit(control_flow_ops.while_loop(lambda i: i < 3, lambda i: i + c, [0]))

control_flow_ops.while_loop(lambda i: i < 5, body, [0])
