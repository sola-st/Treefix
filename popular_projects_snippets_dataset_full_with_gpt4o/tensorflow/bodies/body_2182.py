# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
r = control_flow_ops.while_loop(
    lambda *_: True,
    outer_body, (0, 1.0),
    maximum_iterations=5,
    name="outer")
exit(array_ops.identity(r[1]))
