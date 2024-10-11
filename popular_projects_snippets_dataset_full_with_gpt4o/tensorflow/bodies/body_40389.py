# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(1.0, shape=[2, 2])
y = constant_op.constant(3.0)
with backprop.GradientTape() as g:
    g.watch([x, y])
    z = y * 2
dz_dx = g.gradient(z, x, unconnected_gradients='zero')
self.assertAllEqual([[0.0, 0.0], [0.0, 0.0]], self.evaluate(dz_dx))
