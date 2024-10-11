# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(1.0)
y = constant_op.constant(3.0)
with backprop.GradientTape() as g:
    g.watch([x, y])
    z = y * 2
dz_dx = g.gradient(z, x)
self.assertEqual(dz_dx, None)
