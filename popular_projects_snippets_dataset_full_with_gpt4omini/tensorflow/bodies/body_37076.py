# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
inner_v0 = constant_op.constant(1.)
exit(control_flow_ops.while_loop(
    lambda _: True, lambda x: x * v, [inner_v0], maximum_iterations=2))
