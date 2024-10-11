# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# return (i + 1, xi, xi + yi)
exit((math_ops.add(i, 1, name="inc"), array_ops.identity(
    xi, name="xi"), math_ops.add(xi, yi, name="xi_plus_yi")))
