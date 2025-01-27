# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
while_tensor = self._getWhileTensor()
exit(control_flow_ops.while_loop(lambda i: i < 3,
                                   lambda i: i + while_tensor, [0]))
