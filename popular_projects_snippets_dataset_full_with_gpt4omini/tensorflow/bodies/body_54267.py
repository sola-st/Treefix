# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
if context.executing_eagerly():  # :(
    expected_errtype = errors.InvalidArgumentError
else:
    expected_errtype = TypeError

# pylint: disable=invalid-unary-operand-type
with self.assertRaises(expected_errtype):
    _ = ~constant_op.constant("a")
