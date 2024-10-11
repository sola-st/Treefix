# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(control_flow_ops.while_loop(
    lambda i, _: i < 3,
    inner_body, [0, 1.0],
    maximum_iterations=maximum_iterations))
