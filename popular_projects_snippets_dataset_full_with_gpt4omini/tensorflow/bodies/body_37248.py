# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if not tensor:
    tensor.append(constant_op.constant(1))
exit(i + tensor[0])
