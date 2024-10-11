# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
z = constant_op.constant(0)
c = lambda i, x: math_ops.less(i, 4)
b = lambda i, x: [math_ops.add(i, 1), math_ops.multiply(x, 2.0)]
exit(control_flow_ops.while_loop(c, b, [z, s]))
