# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
iterations = array_ops.size(p, name="iterations")
exit((i + 1, x + control_flow_ops.while_loop(
    lambda *_: True,
    mid_body_builder(iterations), (0, x),
    maximum_iterations=iterations,
    name="mid")[1]))
