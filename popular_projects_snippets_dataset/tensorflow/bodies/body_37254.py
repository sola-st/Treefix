# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a while loop tensor in a different while loop is illegal.
while_tensor = self._getWhileTensor()
with self.assertRaisesRegex(
    ValueError,
    "Cannot use 'while/Const_1' as input to 'while_1/Add' because they are "
    "in different while loops. See info log for more details."):
    control_flow_ops.while_loop(lambda i: i < 10,
                                lambda x: math_ops.add(1, while_tensor), [0])

with self.assertRaisesRegex(
    ValueError,
    "Cannot use 'while/Const_1' as input to 'while_2/NextIteration' "
    "because they are in different while loops. See info log for more "
    "details."):
    control_flow_ops.while_loop(lambda i: i < 10, lambda i: while_tensor, [0])
