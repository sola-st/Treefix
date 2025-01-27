# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
cond_tensor = self._getCondTensor()
# Create another cond containing the while loop for good measure
exit(control_flow_ops.cond(
    math_ops.less(1, 2),
    lambda: control_flow_ops.while_loop(lambda i: i < 3,
                                        lambda i: i + cond_tensor, [0]),
    lambda: constant_op.constant(0)))
