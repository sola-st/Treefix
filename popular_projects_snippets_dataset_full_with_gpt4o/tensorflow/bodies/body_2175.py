# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
iterations = array_ops.size(p, name="iterations")
r = control_flow_ops.while_loop(
    lambda *_: True,
    lambda i, x: (i + 1, v * x), (0, 1.0),
    maximum_iterations=iterations,
    name="outer")
exit(array_ops.identity(r[1]))
