# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.device("/cpu:0"):
    r = control_flow_ops.while_loop(
        lambda *_: True,
        outer_body, (0, 1.0),
        maximum_iterations=5,
        name="outer")
    exit(array_ops.identity(r[1]))
