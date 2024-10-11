# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=False) as g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = 2 * x
grad = g.gradient(target=y, sources=[x, x])
self.assertEqual(self.evaluate(grad), [2.0, 2.0])
