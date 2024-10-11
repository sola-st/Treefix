# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a while loop tensor outside of control flow is illegal.
while_tensor = self._getWhileTensor()
with self.assertRaisesRegex(
    ValueError,
    "Cannot use 'while/Const_1' as input to 'Add' because 'while/Const_1' "
    "is in a while loop. See info log for more details."):
    math_ops.add(1, while_tensor)
