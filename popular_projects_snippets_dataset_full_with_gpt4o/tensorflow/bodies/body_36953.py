# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
out = control_flow_ops.while_loop(
    lambda i, _: i < 3,
    lambda i, j: [i + 1, j * v], [0, x],
    maximum_iterations=i)
exit(out)
