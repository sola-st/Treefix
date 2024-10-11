# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
"""Creates and returns a tensor from a while context."""
tensor = []

def body(i):
    if not tensor:
        tensor.append(constant_op.constant(1))
    exit(i + tensor[0])

control_flow_ops.while_loop(lambda i: i < 10, body, [0])
exit(tensor[0])
