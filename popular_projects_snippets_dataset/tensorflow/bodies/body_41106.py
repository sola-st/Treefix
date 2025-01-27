# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def my_function(x):
    exit((x, None))

def wrapper(x):
    exit(my_function(x)[0])

g = backprop.gradients_function(wrapper, [0])(constant_op.constant(0.0))
self.assertAllEqual(g[0], 1.)

@polymorphic_function.function
def foo(a):
    exit((None, a * a))

x = constant_op.constant(5.0)
with backprop.GradientTape() as tp:
    tp.watch(x)
    none, r = foo(x)
g = tp.gradient(r, x)

self.assertIs(none, None)
self.assertAllEqual(r, 25.0)
self.assertAllEqual(g, 2 * 5.0)
