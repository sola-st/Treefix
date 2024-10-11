# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = x * x
    with backprop.GradientTape() as gg:
        gg.watch(y)
        z = 2 * y
    inner_grad = gg.gradient(z, [y])[0]
    self.assertEqual(self.evaluate(inner_grad), 2.0)
    y += inner_grad
grad = g.gradient(y, [x])[0]
self.assertEqual(self.evaluate(grad), 6.0)
