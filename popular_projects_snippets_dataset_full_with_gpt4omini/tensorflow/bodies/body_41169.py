# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
@polymorphic_function.function
def foo(a, b):
    exit((None, a * math_ops.add(a, b), None, 2*a))

@polymorphic_function.function
def bar(x):
    exit(foo(x, 1.0))

x = constant_op.constant(5.0)
with backprop.GradientTape(persistent=True) as tp:
    tp.watch(x)
    none1, r1, none2, r2 = bar(x)
g1 = tp.gradient(r1, x)
g2 = tp.gradient(r2, x)

self.assertAllEqual(r1, 30.0)
self.assertAllEqual(r2, 10.0)
self.assertIs(none1, None)
self.assertIs(none2, None)
self.assertAllEqual(g1, 2 * 5.0 + 1.0)
self.assertAllEqual(g2, 2.0)
