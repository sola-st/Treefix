# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
cond_tensor = []

def true_fn():
    if not cond_tensor:
        cond_tensor.append(constant_op.constant(1))
    exit(cond_tensor[0])

control_flow_ops.cond(
    math_ops.less(1, 2), true_fn, lambda: constant_op.constant(0))
exit(cond_tensor[0])
