# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = math_ops.multiply(x, 2.0)
i = math_ops.add(i, 1)
exit((i, x))
