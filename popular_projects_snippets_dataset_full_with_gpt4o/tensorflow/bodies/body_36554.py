# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(1.0, name="x")
output = while_v2.while_loop(lambda x: x < 10.0,
                             lambda x: x * 2.0,
                             [x])[0]
while_op = output.op.inputs[0].op
self.assertEqual(while_op.type, "StatelessWhile")
# outputs = [loop_counter, max_iters, x]
self.assertLen(while_op.outputs, 3)

gradients_impl.gradients(output, x)
# while_op should have been rewritten to output intermediates.
# outputs = [loop_counter, max_iters, x, x_accumulator]
self.assertLen(while_op.outputs, 4)

gradients_impl.gradients(output, x)
# Computing the gradient again shouldn't rewrite while_op again.
self.assertLen(while_op.outputs, 4)
