# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
if context.executing_eagerly():
    self.skipTest("tf.gradients not supported in eager.")

x = constant_op.constant([-1., 0., 1.])
g = self.evaluate(gradients.gradients(math_ops.pow(x, 2), x)[0])
self.assertAllClose([-2., 0., 2.], g)
