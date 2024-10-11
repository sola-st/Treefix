# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
r = control_flow_ops.while_loop(
    lambda i, _: i < 2,
    lambda i, x: (i + 1, foo(x, var)),
    [0, 0.0])[1]
exit(gradients_impl.gradients(r, var)[0])
