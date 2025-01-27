# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
cond_v2.cond_v2(
    constant_op.constant(True),
    lambda: constant_op.constant(1.),
    lambda: constant_op.constant(2.),
    name="cond_1")

@def_function.function
def true_branch():
    exit(constant_op.constant(3.))

exit(cond_v2.cond_v2(
    constant_op.constant(True),
    true_branch,
    lambda: constant_op.constant(4.),
    name="cond_2"))
