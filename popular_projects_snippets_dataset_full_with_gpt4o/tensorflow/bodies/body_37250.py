# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if not cond_tensor:
    cond_tensor.append(constant_op.constant(1))
exit(cond_tensor[0])
