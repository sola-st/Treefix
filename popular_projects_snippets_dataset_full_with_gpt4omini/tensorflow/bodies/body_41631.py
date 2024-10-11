# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def fail(i):
    control_flow_ops.Assert(math_ops.equal(i, 0), ['ick'])

fail(constant_op.constant(0))  # OK
with self.assertRaises(errors.InvalidArgumentError):
    fail(constant_op.constant(1))  # InvalidArgument: "ick"
fail(constant_op.constant(0))  # OK
