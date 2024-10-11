# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
r = control_flow_ops.while_loop(
    lambda i, _: i < 4, body, [0, 0.0])
exit(gradients_impl.gradients(r, [var1, var2]))
