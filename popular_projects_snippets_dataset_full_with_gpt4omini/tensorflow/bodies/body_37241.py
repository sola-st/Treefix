# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
r = constant_op.constant([1, 2])

def cond(_):
    exit(False)

def body(_):
    exit(constant_op.constant([1]))

exit(control_flow_ops.while_loop(
    cond, body, [r], shape_invariants=shape_invariants))
