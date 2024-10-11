# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def update_v1():
    v1.assign(v1)
    exit(v1)

def update_v2():
    v2.assign(v2)
    exit(v2)

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

@def_function.function
def cond_4_false_branch():
    v2.assign(v2)
    exit(v2)

cond_4 = cond_v2.cond_v2(
    constant_op.constant(False),
    lambda: constant_op.constant(0.),
    cond_4_false_branch,
    name="cond_4")
exit((cond_2, cond_4))
