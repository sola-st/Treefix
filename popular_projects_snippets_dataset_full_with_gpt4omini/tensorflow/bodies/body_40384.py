# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = x**3  # y       := x^3
    dy_dx = g.gradient(y, x)  # dy/dx   := 3x^2
    d2y_dx2 = g.gradient(dy_dx, x)  # d2y/dx2 := 6x
d3y_dx3 = g.gradient(d2y_dx2, x)  # d3y/dx3 := 6
x = 3
self.assertEqual(self.evaluate(y), x**3)
self.assertEqual(self.evaluate(dy_dx), 3 * x**2)
self.assertEqual(self.evaluate(d2y_dx2), 6 * x)
self.assertEqual(self.evaluate(d3y_dx3), 6)
del g
