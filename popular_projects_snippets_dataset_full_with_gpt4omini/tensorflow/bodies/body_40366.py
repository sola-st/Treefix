# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    x = constant_op.constant(3.0)
    y = constant_op.constant(5.0)
    g.watch(x)
    g.watch(y)
    z = x * x + x * y
grad = g.gradient(target=z, sources=[x, x])
self.assertEqual(self.evaluate(grad), [11.0, 11.0])
grad = g.gradient(target=z, sources=[y, x])
self.assertEqual(self.evaluate(grad), [3.0, 11.0])
