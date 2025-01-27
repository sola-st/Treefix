# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
_, x = control_flow_ops.while_loop(
    lambda j, x: j < 3, inner_body, [0, 0.0])
exit((i + 1, x))
