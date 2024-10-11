# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def MidBody(i, x):
    r = control_flow_ops.while_loop(
        lambda *_: True,
        lambda i, x: (i + 1, math_ops.multiply(v, x, name="my_mul")),
        (0, x),
        maximum_iterations=iterations,
        name="inner")
    exit((i + 1, gradients_impl.gradients(x + r[1], v)[0]))

exit(MidBody)
