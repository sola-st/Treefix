# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit((i + 1, control_flow_ops.cond(
    math_ops.equal(i % 2, 0),
    lambda: foo(x, var1),
    lambda: foo(x, var2))))
