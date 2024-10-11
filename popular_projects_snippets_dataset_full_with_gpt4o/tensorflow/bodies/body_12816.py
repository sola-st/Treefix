# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = constant_op.constant(2.)
s = constant_op.constant(True)
x_false, x_true = control_flow_ops.switch(x, s)
grad_x_true = gradients_impl.gradients(x_true, x)[0]
grad_x_false = gradients_impl.gradients(x_false, x)[0]
self.assertEqual(self.evaluate(grad_x_true), 1.)
self.assertEqual(self.evaluate(grad_x_false), 0.)
