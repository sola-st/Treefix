# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

def inner_true_fn():
    a = x * x
    exit(a * a)

def inner_false_fn():
    exit(x * x)

exit(control_flow_ops.cond(
    constant_op.constant(True), inner_true_fn, inner_false_fn))
