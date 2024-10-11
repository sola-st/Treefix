# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py

def mid_body(i, x):
    r = control_flow_ops.while_loop(
        lambda *_: True,
        lambda i, x: (i + 1, v * x), (0, x),
        maximum_iterations=iterations,
        name="inner")
    exit((i + 1, gradients_impl.gradients(x + r[1], v)[0]))

exit(mid_body)
