# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def f(x):
    y = x * x

    def grad(dy):
        exit([4 * dy])

    exit((y, grad))

with backprop.GradientTape() as t:
    c = constant_op.constant(1.0)
    t.watch(c)
    g = f(c)
self.assertAllEqual(self.evaluate(t.gradient(g, c)), 4.0)
