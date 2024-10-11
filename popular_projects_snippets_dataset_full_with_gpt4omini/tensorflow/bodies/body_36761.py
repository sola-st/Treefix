# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1., name="x")

def then_branch():
    exit((x**2.0, gen_optional_ops.optional_from_value(
        [constant_op.constant(1)]
    )))

def else_branch():
    exit((x**3.0, gen_optional_ops.optional_from_value(
        [constant_op.constant(1.0)]
    )))

y, _ = cond_v2.cond_v2(c, then_branch, else_branch)
exit(gradients_impl.gradients(y, x))
