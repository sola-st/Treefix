# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1.0, name="x")
output = cond_v2.cond_v2(
    constant_op.constant(True), lambda: x * 2.0, lambda: x)
if_op = output.op.inputs[0].op
self.assertEqual(if_op.type, "StatelessIf")
# pylint: disable=g-deprecated-assert
self.assertEqual(len(if_op.outputs), 1)

gradients_impl.gradients(output, x)
# Number of outputs does change because
# 1. `x` is a loop input so does not need to be accumulated.
# 2. 2.0 is a constant so it is not accumulated.
self.assertEqual(len(if_op.outputs), 1)

gradients_impl.gradients(output, x)
# Computing the gradient again shouldn't rewrite if_op again.
self.assertEqual(len(if_op.outputs), 1)
