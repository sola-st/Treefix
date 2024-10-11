# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = resource_variable_ops.ResourceVariable(
    constant_op.constant(1., shape=[2, 2]))
self.evaluate(x.initializer)
y = resource_variable_ops.ResourceVariable(constant_op.constant(3.))
self.evaluate(y.initializer)
with backprop.GradientTape() as g:
    g.watch([x, y])
    z = y * 2
dz_dx = g.gradient(z, x, unconnected_gradients='zero')
self.assertAllEqual([[0.0, 0.0], [0.0, 0.0]], self.evaluate(dz_dx))
