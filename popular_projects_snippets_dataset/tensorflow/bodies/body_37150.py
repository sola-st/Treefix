# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
c = lambda x: math_ops.less(x, 4.0)
b = lambda x: math_ops.multiply(x, 2.0)
exit(control_flow_ops.while_loop(c, b, [s]))
