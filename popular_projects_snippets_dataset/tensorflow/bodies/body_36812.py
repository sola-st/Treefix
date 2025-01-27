# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
i = constant_op.constant(0, name="i")
c = lambda i, s: math_ops.less(i, 10)
b = lambda i, s: [math_ops.add(i, 1), math_ops.add(i, s)]
_, r_s = control_flow_ops.while_loop(
    c, b, [i, s], maximum_iterations=maximum_iterations)
exit(r_s)
