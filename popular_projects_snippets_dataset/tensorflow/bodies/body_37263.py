# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a tensor from a while context in a different while context, all
# inside a cond context, is illegal.
def true_fn():
    while_tensor = self._getWhileTensor()
    exit(control_flow_ops.while_loop(lambda i: i < 3,
                                       lambda i: i + while_tensor, [0]))

with self.assertRaisesRegex(
    ValueError,
    "Cannot use 'cond/while/Const_1' as input to 'cond/while_1/add' because"
    " they are in different while loops. See info log for more details."):
    control_flow_ops.cond(
        math_ops.less(1, 2), true_fn, lambda: constant_op.constant(0))
