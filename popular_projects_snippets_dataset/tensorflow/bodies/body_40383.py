# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = x * x
    z = y * y
dz_dx = g.gradient(z, [x])[0]
self.assertEqual(self.evaluate(dz_dx), 4 * 3 * 3 * 3)
dy_dx = g.gradient(y, [x])[0]
self.assertEqual(self.evaluate(dy_dx), 2 * 3)
del g
