# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1.0, name="x")
y = constant_op.constant(1.0, name="y")

def true_fn():
    y_plus_one = y + 1.
    exit(x * y_plus_one)

output = cond_v2.cond_v2(constant_op.constant(True), true_fn, lambda: x)
if_op = output.op.inputs[0].op
self.assertEqual(if_op.type, "StatelessIf")
# pylint: disable=g-deprecated-assert
self.assertEqual(len(if_op.outputs), 1)

gradients_impl.gradients(output, x)
# if_op should have been rewritten to output `y_plus_one`.
self.assertEqual(len(if_op.outputs), 2)

gradients_impl.gradients(output, x)
# Computing the gradient again shouldn't rewrite if_op again.
self.assertEqual(len(if_op.outputs), 2)
