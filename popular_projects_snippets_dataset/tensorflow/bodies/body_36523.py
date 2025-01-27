# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
iterations = array_ops.size(p, name="iterations")
exit((i + 1, x + control_flow_ops.while_loop(
    lambda *_: True,
    MidBodyBuilder(iterations), (0, x),
    maximum_iterations=iterations,
    name="mid")[1]))
