# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
# In the following test, if x2 = x1 (i.e the objects are the exact same),
# then y is essentially, 2*x1, and dy/dx1 = 2.
# When we had a pure scalar cache in eager, this would be the case. This
# test prevents us from going back to that case.
with backprop.GradientTape(persistent=False) as g:
    x1 = constant_op.constant(3.0)
    x2 = constant_op.constant(3.0)
    g.watch(x1)
    g.watch(x2)
    y = x1 + x2
grad = g.gradient(target=y, sources=[x1])
self.assertEqual(self.evaluate(grad), [1.0])
