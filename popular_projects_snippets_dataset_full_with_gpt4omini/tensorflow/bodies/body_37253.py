# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a while loop tensor in cond is illegal.
while_tensor = self._getWhileTensor()
with self.assertRaisesRegex(
    ValueError, "Cannot use 'while/Const_1' as input to 'cond/Add' because "
    "'while/Const_1' is in a while loop. See info log for more details."):
    # TODO(skyewm): this passes if we return while_tensor directly instead
    # of using it as input to another op.
    control_flow_ops.cond(
        math_ops.less(1, 2), lambda: math_ops.add(1, while_tensor),
        lambda: constant_op.constant(0))
