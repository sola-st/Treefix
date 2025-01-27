# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = constant_op.constant(3.0)
with backprop.GradientTape() as g:
    g.watch(x)
    y = x * x
    z = y * y
dz_dx, dz_dy = g.gradient(z, [x, y])
self.assertEqual(self.evaluate(dz_dx), 108.0)
self.assertEqual(self.evaluate(dz_dy), 18.0)
