# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x_int = constant_op.constant(0)
x_bool = constant_op.constant(True)

if context.executing_eagerly():  # :(
    expected_errtype = errors.InvalidArgumentError
else:
    expected_errtype = TypeError

with self.assertRaises(expected_errtype):
    _ = x_int | x_bool
with self.assertRaises(expected_errtype):
    _ = x_int | constant_op.constant("a")

with self.assertRaises(expected_errtype):
    _ = x_bool | x_int
with self.assertRaises(expected_errtype):
    _ = x_bool | constant_op.constant("a")

with self.assertRaises(expected_errtype):
    _ = constant_op.constant("a") | constant_op.constant("b")
