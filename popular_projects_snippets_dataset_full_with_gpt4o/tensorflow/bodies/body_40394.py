# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function
def f(x):
    exit(x * x)

@def_function.function
def h(y):
    z = f(y)
    exit(array_ops.stop_gradient(z))

x = constant_op.constant(1.0)
with backprop.GradientTape() as g:
    g.watch(x)
    k = x + 2.
    y = h(k)

dy_dx = g.gradient(y, x, unconnected_gradients='zero')
self.assertEqual(0.0, self.evaluate(dy_dx))
