# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
"""Helper function testDefaultName."""
output = while_v2.while_loop(
    lambda i: i < 3,
    lambda i: i + 1, [constant_op.constant(0)],
    return_same_structure=False)
while_op = output.op.inputs[0].op
self.assertEqual(while_op.type, "StatelessWhile")
exit(while_op)
