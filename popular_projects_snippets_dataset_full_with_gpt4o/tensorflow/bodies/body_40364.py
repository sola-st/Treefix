# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
g = backprop.GradientTape()
with g:
    x = constant_op.constant(3.0)
    g.watch(x)
    y = 2 * x
with g:
    z = 2 * y
grad = g.gradient(target=z, sources=[x])
self.assertEqual(self.evaluate(grad), [4.0])
