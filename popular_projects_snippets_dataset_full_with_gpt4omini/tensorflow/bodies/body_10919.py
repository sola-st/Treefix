# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with self.cached_session():
    x = constant_op.constant(1.)
    y = 2 * x
    z = x + y
    totalg = gradients.gradients(z, [x, y])
    self.assertEqual([3.0, 1.0], [g.eval() for g in totalg])
    partialg = gradients.gradients(z, [x, y], stop_gradients=[x, y])
    self.assertEqual([1.0, 1.0], [g.eval() for g in partialg])
