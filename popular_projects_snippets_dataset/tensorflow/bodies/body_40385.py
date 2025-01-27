# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = x * x
    with backprop.GradientTape(persistent=True) as gg:
        gg.watch(y)
        z = 2 * y
    for _ in range(2):
        inner_grad = gg.gradient(z, [y])[0]
        self.assertEqual(self.evaluate(inner_grad), 2.0)
    y += inner_grad
    del gg
grad = g.gradient(y, [x])[0]
self.assertEqual(self.evaluate(grad), 6.0)
grad = g.gradient(z, [x])[0]
self.assertEqual(self.evaluate(grad), 12.0)
del g
