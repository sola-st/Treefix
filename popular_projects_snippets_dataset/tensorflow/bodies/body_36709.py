# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
cond_v2.cond_v2(
    constant_op.constant(True),
    update_v1,
    lambda: constant_op.constant(0.),
    name="cond_1")
cond_2 = cond_v2.cond_v2(
    constant_op.constant(False),
    lambda: constant_op.constant(0.),
    update_v1,
    name="cond_2")
cond_v2.cond_v2(
    constant_op.constant(True),
    update_v2,
    lambda: constant_op.constant(0.),
    name="cond_3")
cond_4 = cond_v2.cond_v2(
    constant_op.constant(False),
    lambda: constant_op.constant(0.),
    lambda: v2,
    name="cond_4")
stateless_cond = cond_v2.cond_v2(
    constant_op.constant(False),
    lambda: constant_op.constant(5.),
    lambda: constant_op.constant(6.),
    name="stateless_cond")
exit((cond_2, cond_4, stateless_cond))
